import pygame
class Text():
    font = pygame.font.Font('data/fonts/pong.ttf',48)
    font_size_2 = pygame.font.Font('data/fonts/pong.ttf',32)
    text2X = 250
    text2Y = 90
    text3X = 360
    text3Y = 10
    def __init__(self):
        pass
    def show_00(self,x,y,screen):
        ket =self.font.render("|00>",True,(255,255,255))
        screen.blit(ket, (x,y))
    def show_01(self,x,y,screen):
        ket =self.font.render("|01>",True,(255,255,255))
        screen.blit(ket, (x,y))
    def show_10(self,x,y,screen):
        ket =self.font.render("|10>",True,(255,255,255))
        screen.blit(ket, (x,y))
    def show_11(self,x,y,screen):
        ket =self.font.render("|11>",True,(255,255,255))
        screen.blit(ket, (x,y))
    def show_000(self,x,y,screen):
        ket =self.font_size_2.render("|000>",True,(255,255,255))
        screen.blit(ket, (x,y))
    def show_001(self,x,y,screen):
        ket =self.font_size_2.render("|001>",True,(255,255,255))
        screen.blit(ket, (x,y))
    def show_010(self,x,y,screen):
        ket =self.font_size_2.render("|010>",True,(255,255,255))
        screen.blit(ket, (x,y))
    def show_011(self,x,y,screen):
        ket =self.font_size_2.render("|011>",True,(255,255,255))
        screen.blit(ket, (x,y))
    def show_100(self,x,y,screen):
        ket =self.font_size_2.render("|100>",True,(255,255,255))
        screen.blit(ket, (x,y))
    def show_101(self,x,y,screen):
        ket =self.font_size_2.render("|101>",True,(255,255,255))
        screen.blit(ket, (x,y))
    def show_110(self,x,y,screen):
        ket =self.font_size_2.render("|110>",True,(255,255,255))
        screen.blit(ket, (x,y))
    def show_111(self,x,y,screen):
        ket =self.font_size_2.render("|111>",True,(255,255,255))
        screen.blit(ket, (x,y))
    def display_text(self,screen):
        self.show_00(self.text2X,self.text2Y,screen)
        self.show_01(self.text2X,self.text2Y+(120*1),screen)
        self.show_10(self.text2X,self.text2Y+(120*2),screen)
        self.show_11(self.text2X,self.text2Y+(120*3),screen)
        self.show_000(self.text3X+(82*0),self.text3Y,screen)
        self.show_001(self.text3X+(82*1),self.text3Y,screen)
        self.show_010(self.text3X+(82*2),self.text3Y,screen)
        self.show_011(self.text3X+(82*3),self.text3Y,screen)
        self.show_100(self.text3X+(82*4),self.text3Y,screen)
        self.show_101(self.text3X+(82*5),self.text3Y,screen)
        self.show_110(self.text3X+(82*6),self.text3Y,screen)
        self.show_111(self.text3X+(82*7),self.text3Y,screen)