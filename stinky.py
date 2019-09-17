from pygame.sprite import Sprite
import pygame
from random import choice
class Stinky(Sprite):
    def __init__(self,screen):
        super(Stinky, self).__init__()
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.image1 = pygame.image.load('images/Stinky_turn1.png')
        self.image2 = pygame.image.load('images/Stinky_turn2.png')
        self.image3 = pygame.image.load('images/Stinky_turn3.png')
        self.image4 = pygame.image.load('images/Stinky_turn4.png')
        self.image5 = pygame.image.load('images/Stinky_turn5.png')
        self.image6 = pygame.image.load('images/Stinky_turn6.png')
        self.image7 = pygame.image.load('images/Stinky_turn7.png')
        self.image8 = pygame.image.load('images/Stinky_turn8.png')
        self.rect = self.image1.get_rect()
        self.images=[self.image1,self.image2,self.image3,self.image4,
                     self.image5,self.image6,self.image7,self.image8]
        self.x = float(self.rect.x)
        #定位
        self.rect.left = self.screen_rect.left
        self.rect.centery = choice([100, 300, 500])
        self.number=0
        self.speed = 10
    def update(self):
        self.x+=10
        self.rect.x = self.x

    def blit(self):
        if self.number ==9:
            self.number=0
        else:
            self.number+=1
        self.screen.blit(self.images[self.number//5],self.rect)



