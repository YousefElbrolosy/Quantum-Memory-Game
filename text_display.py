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
    def show_00(self,x,y,screen,color):
        ket =self.font.render("|00>",True,color)
        screen.blit(ket, (x,y))
    def show_01(self,x,y,screen,color):
        ket =self.font.render("|01>",True,color)
        screen.blit(ket, (x,y))
    def show_10(self,x,y,screen,color):
        ket =self.font.render("|10>",True,color)
        screen.blit(ket, (x,y))
    def show_11(self,x,y,screen,color):
        ket =self.font.render("|11>",True,color)
        screen.blit(ket, (x,y))
    def show_000(self,x,y,screen,color):
        ket =self.font_size_2.render("|000>",True,color)
        screen.blit(ket, (x,y))
    def show_001(self,x,y,screen,color):
        ket =self.font_size_2.render("|001>",True,color)
        screen.blit(ket, (x,y))
    def show_010(self,x,y,screen,color):
        ket =self.font_size_2.render("|010>",True,color)
        screen.blit(ket, (x,y))
    def show_011(self,x,y,screen,color):
        ket =self.font_size_2.render("|011>",True,color)
        screen.blit(ket, (x,y))
    def show_100(self,x,y,screen,color):
        ket =self.font_size_2.render("|100>",True,color)
        screen.blit(ket, (x,y))
    def show_101(self,x,y,screen,color):
        ket =self.font_size_2.render("|101>",True,color)
        screen.blit(ket, (x,y))
    def show_110(self,x,y,screen,color):
        ket =self.font_size_2.render("|110>",True,color)
        screen.blit(ket, (x,y))
    def show_111(self,x,y,screen,color):
        ket =self.font_size_2.render("|111>",True,color)
        screen.blit(ket, (x,y))
    def display_text(self,screen,color):
        self.show_00(self.text2X,self.text2Y,screen,color)
        self.text2Y+=(120*1)
        self.show_01(self.text2X,self.text2Y,screen,color)
        self.text2Y+=(120*1)
        self.show_10(self.text2X,self.text2Y,screen,color)
        self.text2Y+=(120*1)
        self.show_11(self.text2X,self.text2Y,screen,color)
        self.show_000(self.text3X,self.text3Y,screen,color)
        self.text3X+=(82*1)
        self.show_001(self.text3X,self.text3Y,screen,color)
        self.text3X+=(82*1)
        self.show_010(self.text3X,self.text3Y,screen,color)
        self.text3X+=(82*1)
        self.show_011(self.text3X,self.text3Y,screen,color)
        self.text3X+=(82*1)
        self.show_100(self.text3X,self.text3Y,screen,color)
        self.text3X+=(82*1)
        self.show_101(self.text3X,self.text3Y,screen,color)
        self.text3X+=(82*1)
        self.show_110(self.text3X,self.text3Y,screen,color)
        self.text3X+=(82*1)
        self.show_111(self.text3X,self.text3Y,screen,color)