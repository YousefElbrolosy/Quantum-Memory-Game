"""
import pygame
from text_display import Text
pygame.init()
screen = pygame.display.set_mode((500,500))
fps = 60
timer = pygame.time.Clock()
font = pygame.font.Font('data/fonts/pong.ttf',48)


button = pygame.Rect(left = 10, top = 10, width = 200, height= 100)
pygame.draw.rect(screen, (255,255,255), button, 0, 5)
test = font.render("test",True,(255,255,255))
"""
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
        button_text = self.font.render(self.text,True,'white')
        button_rect = pygame.rect.Rect((xpos,ypos),(self.width,self.height))
                                                            #edge_width
        pygame.draw.rect(self.screen,self.color,button_rect , 0 ,5)
        pygame.draw.rect(self.screen,self.border_color,button_rect , self.border_width ,5)
        self.screen.blit(button_text,(xpos+5,ypos+5))

    def press(self):
        self.pressed = True
        #border = -1 means no border = 0 all border
        self.border_width = -1

    def un_press(self):
        self.pressed = False
        self.color = self.original_color
        self.border_width = self.original_border_width
"""
exit = False 
while not exit: 
    screen.fill((0,0,0))
    #text
    row_button = Button("Row", 100, 100 ,10 ,10,screen,text_display.font)
    col_button = Button("Column", 200 ,100 ,10 ,150,screen,text_display.font)
    #update game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
        elif event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_LSHIFT):
                col_button.pressed = True
                col_flag = True
                
            elif (event.key == pygame.K_RSHIFT):
                row_button.pressed = True
                print("pressed succ")
                row_flag = True
    pygame.display.flip()
    
"""

