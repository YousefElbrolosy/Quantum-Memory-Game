import pygame
class Button():
    def __init__(self,text,width,height,color,border_color,border_width,screen,font) -> None:
        self.text = text
        self.width = width
        self.height = height
        self.color = color
        self.original_color = color
        self.border_color = border_color
        self.border_width = border_width
        self.original_border_width = border_width
        self.enabled = True
        self.pressed = False
        self.screen = screen
        self.font = font

    def add_button(self,xpos,ypos):
        button_text = self.font.render(self.text,True,'black')
        button_rect = pygame.rect.Rect((xpos,ypos),(self.width,self.height))
                                                            #edge_width
        pygame.draw.rect(self.screen,self.color,button_rect , 0 ,5)
        pygame.draw.rect(self.screen,self.border_color,button_rect , self.border_width ,5)
        self.screen.blit(button_text,(xpos+10,ypos+(self.height/2)-15))

    def press(self):
        self.pressed = True
        #border = -1 means no border = 0 all border
        self.color = self.original_color
        self.border_width = self.original_border_width
        
        self.enabled = False

    def un_press(self):
        self.pressed = False
        self.border_width = -1
        self.enabled = True

