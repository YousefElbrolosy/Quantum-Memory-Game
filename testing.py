from button import Button
import pygame
pygame.init()
screen = pygame.display.set_mode((500,500))
fps = 60
timer = pygame.time.Clock()
font = pygame.font.Font('data/fonts/pong.ttf',48)
exit = False
button_1 = Button("test",100,100,'gray','dark gray',4,screen,font)
while not exit:
    screen.fill((255,255,255))
    button_1.add_button(10,10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                exit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
                  button_1.press()
            if event.key == pygame.K_r:
                  button_1.un_press()

    timer.tick(60)
    pygame.display.flip()