import pygame.font
class Gold_Coin():
    def __init__(self,screen,stats):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.stats = stats
        self.text_color = (12,12,12)
        self.msg = self.stats.score
        self.width,self.height = 200,50
        self.font = pygame.font.Font(None,48)
        self.rect = pygame.Rect(0,0,self.width,self.height)
        self.rect.topleft =(0,0)
        self.image = self.font.render(str(self.msg),True,self.text_color)
    def get_image(self):
        '''将得分转换为一幅渲染的图像'''
        rounded_score = int(round(self.stats.gold, -1))
        score_str = '{:,}'.format(rounded_score)  # 这里是在告诉Python在数字间插入逗号
        score_str = 'gold: ' + score_str
        self.score_image = self.font.render(score_str, True, self.text_color,None)
        # 将得分放在屏幕右上角
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20
    def show_gold(self):
        self.screen.blit(self.score_image, self.score_rect)
