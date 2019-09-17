import pygame
class Picture():
    def __init__(self,screen,file):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.image = pygame.image.load(file)
        self.rect = self.image.get_rect()
        #定位
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = 100
        #计时装置
        self.number = 0

    def blit(self):
        if self.number <=100:
            self.screen.blit(self.image,self.rect)
            self.number+=1