import pygame
from pygame.sprite import Sprite
class Snow_Pea(Sprite):
    def __init__(self,screen):
        super(Snow_Pea, self).__init__()
        self.image = pygame.image.load('images/SnowPea.gif')
        self.rect = self.image.get_rect()
        #火焰特效包
        self.image_fire1 = pygame.image.load('images/Torchwood_fire1a.png')
        self.image_fire2 = pygame.image.load('images/Torchwood_fire1b.png')
        self.image_fire3 = pygame.image.load('images/Torchwood_fire1c.png')
        self.image_fires = [self.image_fire1,self.image_fire2,self.image_fire3]
        self.rect_fire = self.image_fire1.get_rect()

        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        #设置初始位置
        self.rect.left = self.screen_rect.left+50
        self.rect.centery = self.screen_rect.centery
        self.rect_fire.centerx = self.rect.centerx
        self.rect_fire.centery = self.rect.centery-60
        #设置速度
        self.speed_x = 100
        self.speed_y = 200
        #移动标志
        self.move_left = False
        self.move_right = False
        self.move_up = False
        self.move_down = False
        self.number = 0
    def blitme(self):
        '''绘制寒冰豌豆'''
        if self.number==8:
            self.number=0
        else:
            self.number+=1
        self.screen.blit(self.image,self.rect)
        self.screen.blit(self.image_fires[self.number//3],self.rect_fire)
    def update(self):
        if self.move_left and self.rect.left-self.speed_x>0:
            self.rect.centerx-=self.speed_x
            self.move_left = False
        if self.move_right and self.rect.right+self.speed_x<self.screen_rect.right:
            self.rect.centerx+=self.speed_x
            self.move_right = False
        if self.move_up and self.rect.top-self.speed_y>0:
            self.rect.centery-=self.speed_y
            self.move_up = False
        if self.move_down and self.rect.bottom+self.speed_y<self.screen_rect.bottom:
            self.rect.centery+=self.speed_y
            self.move_down = False
        self.rect_fire.centerx = self.rect.centerx
        self.rect_fire.centery = self.rect.centery - 60
