import pygame
import sys
from bullet import Bullet
from zombie import Zombie,Buckethead_Zombie,Float_Zombie
from stinky import Stinky
from golden_coin import Gold_Coin


def background_get_rect(weight,height):
    '''加载背景图片,音乐,并得到其矩形'''
    background_image = pygame.image.load('images/background.png')
    rescaled_background = pygame.transform.scale(background_image,(weight,height))
    return rescaled_background


def check_events(snow_pea,stats,screen,stinkies,start_button):
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_q:
                sys.exit()
            if event.key==pygame.K_UP:
                snow_pea.move_up=True
            if event.key==pygame.K_DOWN:
                snow_pea.move_down=True
            if event.key==pygame.K_LEFT:
                snow_pea.move_left=True
            if event.key==pygame.K_RIGHT:
                snow_pea.move_right=True
            if event.key==pygame.K_SPACE and not stats.game_active:
                stats.game_active=True
                stats.win=True
                stats.restart()
                pygame.mixer.music.load('music/the start of a travel.mp3')
                pygame.mixer.music.play(-1,0.0)
            if event.key==pygame.K_a:
                fire_stinky(stats, screen, stinkies)
        if event.type==pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            button_clicked = start_button.rect.collidepoint(mouse_x, mouse_y)
            if button_clicked and not stats.game_active:
                stats.game_active = True
                stats.win = True
                stats.restart()
                pygame.mixer.music.load('music/the start of a travel.mp3')
                pygame.mixer.music.play(-1, 0.0)

        #elif event.type==pygame.MOUSEBUTTONDOWN:

def fire_stinky(stats,screen,stinkies):
    if stats.gold>=500:
        new_stinky = Stinky(screen)
        stinkies.add(new_stinky)
        stats.gold-=500








def update_screen(snow_pea,screen,bullets,background,zombies,stats,start_button,ai_settings,buckethead_zombies,stinkies,picture1,float_zombies,picture2):

    screen.fill((100,100,100))
    screen.blit(background, (0, 0))

    snow_pea.update()
    snow_pea.blitme()
    gold = Gold_Coin(screen, stats)
    gold.get_image()
    gold.show_gold()

    for bullet in bullets.sprites():
        bullet.blit()
    for zombie in zombies.sprites():
        zombie.blit()
    for buckethead_zombie in buckethead_zombies:
        buckethead_zombie.blit()
    for float_zombie in float_zombies:
        float_zombie.blit()
    for stinky in stinkies.sprites():
        stinky.blit()
    if not stats.win:
        image = pygame.image.load('images/ZombiesWon.jpg')
        rescaled_image = pygame.transform.scale(image, (ai_settings.screen_width, ai_settings.screen_height))
        rect = rescaled_image.get_rect()
        screen_rect = screen.get_rect()
        rect.center = screen_rect.center
        screen.blit(rescaled_image, rect)
    if not stats.game_active:
        start_button.draw_button()
    if stats.level_2:
        picture1.blit()
    if stats.level_3:
        picture2.blit()
    if stats.happy_ending:
        # 清空
        zombies.empty()
        bullets.empty()
        buckethead_zombies.empty()
        float_zombies.empty()

        # 植物归位
        screen_rect = screen.get_rect()
        snow_pea.rect.left = screen_rect.left + 50
        snow_pea.rect.centery = screen_rect.centery
        #胜利画面
        he_image1 = pygame.image.load('images/saber.jpg')
        he_image2 = pygame.image.load('images/Tallnut_cracked1.png')
        rescaled_image2 = pygame.transform.scale(he_image2,(200,250))
        he_rect1 = he_image1.get_rect()
        he_rect2 = rescaled_image2.get_rect()
        he_rect2.centerx = 500
        he_rect2.centery = 150
        screen.blit(he_image1,he_rect1)
        screen.blit(rescaled_image2,he_rect2)
    # 让最新绘制的屏幕可见
    pygame.display.flip()

def update_events(bullets,screen,zombies,buckethead_zombies,stinkies,float_zombies):
    screen_rect=screen.get_rect()
    for bullet in bullets:
        bullet.update()
        if bullet.rect.left>=screen_rect.right:
            bullets.remove(bullet)
    for stinky in stinkies:
        stinky.update()
        if stinky.rect.left>=screen_rect.right:
            stinkies.remove(stinky)
    pygame.sprite.groupcollide(stinkies, zombies, False, True)
    pygame.sprite.groupcollide(stinkies, buckethead_zombies, False, True)
    pygame.sprite.groupcollide(stinkies, float_zombies, True, True)
    for zombie in zombies:
        zombie.update()
    for buckethead_zombie in buckethead_zombies:
        buckethead_zombie.update()
    for float_zombie in float_zombies:
        float_zombie.update()


def check_bullet_zombie_collisions(bullets, zombies,stats,buckethead_zombies,float_zombies):
    for bullet in bullets:
        for zombie in zombies:
            if bullet.rect.colliderect(zombie.rect):
                bullets.remove(bullet)
                if zombie.life==0:
                    zombies.remove(zombie)
                    stats.score+=50
                    stats.gold+=50
                else:
                    zombie.life-=1
                    zombie.speed_x*=0.8
        for buckethead_zombie in buckethead_zombies:
            if bullet.rect.colliderect(buckethead_zombie.rect):
                bullets.remove(bullet)
                if buckethead_zombie.life==0:
                    buckethead_zombies.remove(buckethead_zombie)
                    stats.score+=100
                    stats.gold+=100
                else:
                    buckethead_zombie.life-=1
                    buckethead_zombie.speed_x*=0.8
        for float_zombie in float_zombies:
            if bullet.rect.colliderect(float_zombie.rect):
                bullets.remove(bullet)
                if float_zombie.life==0:
                    float_zombies.remove(float_zombie)
                    stats.score+=200
                    stats.gold+=200
                else:
                    float_zombie.life-=1
                    float_zombie.speed_x*=1.1

def check_pea_zombie_collision(zombies,snow_pea,ai_settings,stats,screen,bullets,buckethead_zombies,float_zombies):
    for zombie in zombies:
        if zombie.rect.colliderect(snow_pea.rect):
            game_over(stats, screen, zombies, bullets, snow_pea, buckethead_zombies,float_zombies)
    for buckethead_zombie in buckethead_zombies:
        if buckethead_zombie.rect.colliderect(snow_pea.rect):
            game_over(stats, screen, zombies, bullets, snow_pea, buckethead_zombies,float_zombies)
    for float_zombie in float_zombies:
        if float_zombie.rect.colliderect(snow_pea.rect):
            game_over(stats, screen, zombies, bullets, snow_pea, buckethead_zombies,float_zombies)

def check_courtyard_zombie(zombies,ai_settings,stats,screen,bullets,snow_pea, buckethead_zombies,float_zombies):
    for zombie in zombies:
        if zombie.rect.right<=0:
            zombies.remove(zombie)
            if stats.life<=0:
                game_over(stats, screen, zombies, bullets, snow_pea, buckethead_zombies,float_zombies)
            else:
                stats.life-=1
    for zombie in buckethead_zombies:
        if zombie.rect.right<=0:
            buckethead_zombies.remove(zombie)
            if stats.life<=0:
                game_over(stats, screen, zombies, bullets, snow_pea, buckethead_zombies,float_zombies)
            else:
                stats.life-=1
    for zombie in float_zombies:
        if zombie.rect.right<=0:
            float_zombies.remove(zombie)
            if stats.life<=0:
                game_over(stats, screen, zombies, bullets, snow_pea, buckethead_zombies,float_zombies)
            else:
                stats.life-=1



def game_over(stats,screen,zombies,bullets,snow_pea,buckethead_zombies,float_zombies):
    stats.game_active=False
    stats.win=False
    #永远的满月
    pygame.mixer.music.load('music/上海アリス幻樂団 - 永远の満月.mp3')
    pygame.mixer.music.play(-1,0.0)
    #清空
    zombies.empty()
    bullets.empty()
    buckethead_zombies.empty()
    float_zombies.empty()


    #植物归位
    screen_rect=screen.get_rect()
    snow_pea.rect.left = screen_rect.left + 50
    snow_pea.rect.centery = screen_rect.centery

def fire(stats,ai_settings,snow_pea,screen,bullets,zombies,buckethead_zombies,float_zombies):
    # 自动发射豌豆,生成僵尸
    stats.bullet_accumulate += 1
    if stats.bullet_accumulate >= ai_settings.bullet_max_accumulate:
        stats.bullet_accumulate = 0
        new_bullet = Bullet(snow_pea, screen)
        bullets.add(new_bullet)
    stats.zombie_accumulate += 1
    if stats.zombie_accumulate >= ai_settings.zombie_max_accumulate and stats.zombie_number > 0:
        stats.zombie_number -= 1
        stats.zombie_accumulate = 0
        new_zombie = Zombie(screen)
        zombies.add(new_zombie)
    stats.buckethead_zombie_accumulate +=1
    if stats.level_2:
        if stats.buckethead_zombie_accumulate >=ai_settings.buckethead_zombie_max_accumulate and stats.buckethead_zombie_number >0:
            stats.buckethead_zombie_number -= 1
            stats.buckethead_zombie_accumulate = 0
            new_zombie = Buckethead_Zombie(screen)
            buckethead_zombies.add(new_zombie)
    stats.float_zombie_accumulate +=1
    if stats.level_3:
        if stats.float_zombie_accumulate >=ai_settings.float_zombie_max_accumulate and stats.float_zombie_number >0:
            stats.float_zombie_number -= 1
            stats.float_zombie_accumulate = 0
            new_zombie = Float_Zombie(screen)
            float_zombies.add(new_zombie)

def level_up(stats,zombies,buckethead_zombies,float_zombies):
    '''检测升级'''
    if stats.score >= 850 and not stats.level_2 and stats.game_active==True:
        stats.zombie_number += 15
        stats.level_2 = True
        pygame.mixer.music.load('music/森永真由美 - 灼熱のユートピア.mp3')
        pygame.mixer.music.play(-1, 0.0)
    if stats.score>=2450 and not stats.level_3 and stats.game_active==True:
        stats.zombie_number +=20
        stats.buckethead_zombie_number +=15
        stats.level_3 = True
        pygame.mixer.music.load('music/Sound Horizon - 红莲の弓矢.mp3')
        pygame.mixer.music.play(-1, 5.0)
    if stats.zombie_number+stats.buckethead_zombie_number+stats.float_zombie_number ==0 and len(zombies)+len(buckethead_zombies)+len(float_zombies)==0 and stats.happy_ending==False:
        stats.game_active = False
        stats.happy_ending=True
        pygame.mixer.music.load('music/川井憲次 - 骑士王の夸り.MP3')
        pygame.mixer.music.play(-1, 0.0)




