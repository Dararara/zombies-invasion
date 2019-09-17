import pygame
from settings import Settings
import game_functions as gf
from snow_pea import Snow_Pea
from pygame.sprite import Group
from button import Button
from game_stats import GameStats
from stinky import Stinky
from golden_coin import Gold_Coin
from picture import Picture
from zombie import Float_Zombie

def run_game():
    pygame.init()
    ai_settings=Settings()
    stats = GameStats()
    stats.restart()
    #载入屏幕,背景音乐
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    screen
    pygame.display.set_caption('zombies invasion!'.title())
    pygame.mixer.music.load('music/佐藤直紀 - 3年E組の不安.mp3')
    pygame.mixer.music.play(-1,0.0)#此处高能BGM,左边为循环次数,右边为开始时间,从音乐的哪里开始
    mainclock = pygame.time.Clock()
    #载入背景并绘制
    background = gf.background_get_rect(ai_settings.screen_width,ai_settings.screen_height)
    screen.blit(background,(0,0))
    #绘制寒冰射手
    snow_pea = Snow_Pea(screen)
    snow_pea.blitme()
    #载入开始键
    start_button=Button(screen,'start')
    picture1 = Picture(screen,'images/APPROACHING.png')
    picture2 = Picture(screen,'images/Credits_wearetheundead.jpg')
    #制作空弹夹
    bullets=Group()
    stinkies = Group()
    zombies=Group()
    buckethead_zombies = Group()
    float_zombies = Group()

    mainclock.tick(ai_settings.fps)

    #开始游戏主循环
    while True:
        gf.check_events(snow_pea,stats,screen,stinkies,start_button)
        gf.update_screen(snow_pea, screen, bullets, background, zombies, stats, start_button,ai_settings,buckethead_zombies,stinkies,picture1,float_zombies,picture2)
        gf.level_up(stats,zombies,buckethead_zombies,float_zombies)
        gf.update_events(bullets, screen, zombies,buckethead_zombies,stinkies,float_zombies)
        if stats.game_active:
            gf.fire(stats,ai_settings,snow_pea,screen,bullets,zombies,buckethead_zombies,float_zombies)
            #检测碰撞
            gf.check_bullet_zombie_collisions(bullets, zombies,stats,buckethead_zombies,float_zombies)
            gf.check_pea_zombie_collision(zombies,snow_pea,ai_settings,stats,background,bullets,buckethead_zombies,float_zombies)
            gf.check_courtyard_zombie(zombies,ai_settings,stats,screen,bullets,snow_pea, buckethead_zombies,float_zombies)







run_game()