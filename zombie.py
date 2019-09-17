import pygame
from pygame.sprite import Sprite
from random import choice
class Zombie(Sprite):
    def __init__(self,screen):
        super(Zombie, self).__init__()
        self.weight = 100
        self.height = 100
        self.image = pygame.image.load('images/ConeheadZombieAttack.gif')
        self.rect = self.image.get_rect()
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        #定位
        self.rect.left = self.screen_rect.right
        self.rect.centery = choice([100,300,500])
        #速度
        self.speed_x = 0.3
        self.x=float(self.rect.x)
        #生命值
        self.life=6
    def update(self):
        self.x -= self.speed_x
        self.rect.x = self.x
    def blit(self):
        self.screen.blit(self.image,self.rect)
        
class Buckethead_Zombie(Sprite):
    def __init__(self,screen):
        super(Buckethead_Zombie, self).__init__()
        self.screen=screen
        self.screen_rect = screen.get_rect()
        self.image = pygame.image.load('images/BucketheadZombie.gif')
        self.image1 = pygame.image.load('images/Zombie_bucket1.png')
        self.image2 = pygame.image.load('images/Zombie_bucket2.png')
        self.image3 = pygame.image.load('images/Zombie_bucket3.png')
        self.rect = self.image.get_rect()
        self.image_rect = self.image1.get_rect()
        self.speed_x = 0.5

        #定位
        self.rect.left = self.screen_rect.right
        self.rect.centery = choice([100, 300, 500])
        self.image_rect.centerx = self.rect.centerx
        self.image_rect.y = self.rect.y
        self.x = float(self.rect.x)
        #生命值
        self.life = 10
    def blit(self):
        if self.life>=7:
            self.screen.blit(self.image,self.rect)
            self.screen.blit(self.image1,self.image_rect)
        elif self.life>=3:
            self.screen.blit(self.image, self.rect)
            self.screen.blit(self.image2, self.image_rect)
        else:
            self.screen.blit(self.image, self.rect)
            self.screen.blit(self.image3, self.image_rect)
    def update(self):
        self.x -= self.speed_x
        self.rect.x = self.x
        self.image_rect.centerx = self.rect.centerx

class Float_Zombie(Sprite):
    def __init__(self,screen):
        super(Float_Zombie, self).__init__()
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.image = pygame.image.load('images/tree.png')
        self.image1 = pygame.image.load('images/Zombie_screendoor1.png')
        self.image2 = pygame.image.load('images/Zombie_screendoor2.png')
        self.image3 = pygame.image.load('images/Zombie_screendoor3.png')
        self.images = [self.image1,self.image2,self.image3]
        self.rect = self.image.get_rect()
        self.image1_rect = self.image1.get_rect()
        #生命值
        self.life = 2
        #位置
        self.rect.left = self.screen_rect.right
        self.rect.centery = choice([100, 300, 500])
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        #速度
        self.speed_x = 1
        self.speed_y = [5,4,3,2,1,0,-1,-2,-3,-4,-5]
        self.number = 0

    def update(self):
        if self.number ==21:
            self.number=0
        else:
            self.number+=1
        self.x -= self.speed_x
        self.y += self.speed_y[self.number//2]
        self.rect.x = self.x
        self.rect.y = self.y
        self.image1_rect.x = self.rect.x
        self.image1_rect.y = self.rect.y
    def blit(self):
        if self.life>=7:
            self.screen.blit(self.image,self.rect)
            self.screen.blit(self.image1,self.image1_rect)
        elif self.life>=3:
            self.screen.blit(self.image, self.rect)
            self.screen.blit(self.image2, self.image1_rect)
        else:
            self.screen.blit(self.image, self.rect)
            self.screen.blit(self.image3, self.image1_rect)
