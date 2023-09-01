import pygame
class Text():
    font = pygame.font.Font('data/fonts/pong.ttf',48)
    font_size_2 = pygame.font.Font('data/fonts/pong.ttf',32)
    text2X = 250
    text2Y = 90
    text3X = 360
    text3Y = 10
    color00 = (255,255,255)
    color01 = (255,255,255)
    color10 = (255,255,255)
    color11 = (255,255,255)
    color000 = (255,255,255)
    color001 = (255,255,255)
    color010 = (255,255,255)
    color011 = (255,255,255)
    color100 = (255,255,255)
    color101 = (255,255,255)
    color110 = (255,255,255)
    color111 = (255,255,255)
    color_list_2 = [color00,color01,color10,color11]
    color_list_3 = [color000,color001,color010,color011,color100,color101,color110,color111]
    state_list_2 = ["|00>","|01>","|10>","|11>"]
    state_list_3 = ["|000>","|001>","|010>","|011>","|100>","|101>","|110>","|111>"]
    def __init__(self):
        pass
    def gen2(self,screen):
        for i in range(len(self.state_list_2)):
            ket = self.font.render(self.state_list_2[i],True,self.color_list_2[i])
            screen.blit(ket,(self.text2X,self.text2Y))
            self.text2Y+=(120*1)
    def gen3(self,screen):
        for i in range(len(self.state_list_3)):
            ket = self.font_size_2.render(self.state_list_3[i],True,self.color_list_3[i])
            screen.blit(ket,(self.text3X,self.text3Y))
            self.text3X+=(82*1)
    def display_grid(self,screen):
        self.gen2(screen)
        self.gen3(screen)
    def reset(self):
        self.color_list_2 = [self.color00,self.color01,self.color10,self.color11]
        self.color_list_3 = [self.color000,self.color001,self.color010,self.color011,self.color100,self.color101,self.color110,self.color111]