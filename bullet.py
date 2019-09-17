import pygame
from pygame.sprite import Sprite
class Bullet(Sprite):
    def __init__(self,snow_pea,screen):
        super().__init__()
        self.screen=screen
        self.image1 = pygame.image.load('images/FirePea_flame1.png')
        self.image2 = pygame.image.load('images/FirePea_flame2.png')
        self.image3 = pygame.image.load('images/FirePea_flame3.png')
        self.images = [self.image1,self.image2,self.image3]
        self.rect = self.image1.get_rect()
        self.speed = 3
        self.number = 0

        #定位
        self.rect.right=snow_pea.rect.right
        self.rect.centery = snow_pea.rect.centery-15
        self.direction = 1
        self.centerx=float(self.rect.centerx)
    def blit(self):
        if self.number==8:
            self.number=0
        else:
            self.number+=1
        self.screen.blit(self.images[self.number//3],self.rect)
    def update(self):
        self.centerx+=self.speed
        self.rect.centerx=self.centerx


