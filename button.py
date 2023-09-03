"""
import pygame
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
    def __init__(self,text,width,height,xpos,ypos,screen,font) -> None:
        self.text = text
        self.width = width
        self.height = height
        self.xpos = xpos
        self.ypos = ypos
        self.enabled = True
        self.pressed = False
        self.screen = screen
        self.font = font
        self.add_button(self.xpos,self.ypos)

    def add_button(self,xpos,ypos):
        button_text = self.font.render(self.text,True,'black')
        button_rect = pygame.rect.Rect((xpos,ypos),(self.width,self.height))
                                                 #edge_width 
        if self.pressed == True and self.enabled == True:
            pygame.draw.rect(self.screen,'dark gray',button_rect , 0 ,5)
        pygame.draw.rect(self.screen,'gray',button_rect , 0 ,5)
        pygame.draw.rect(self.screen,'black',button_rect , 2 ,5)
        self.screen.blit(button_text,(xpos+5,ypos+5))

         
         

"""
exit = False 
while not exit: 
    screen.fill('white')
    timer.tick(fps)
    my_button = Button("test",100,100,10,10)
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = True
    pygame.display.flip()
    

class Button():

    def __init__(self,text,posX,posY,size):
        self.text = text
        self.posX = posX
        self.posY = posY
        self.size = size
    
    def add_button(self,screen):
        button = pygame.rect.Rect(left = self.posX, top = self.posY, width = 200, height= 100)
        pygame.draw.rect(screen, (255,255,255), button, 0, 5)

"""
