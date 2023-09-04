from button import Button
import pygame
pygame.init()
screen = pygame.display.set_mode((500,500))
fps = 60
timer = pygame.time.Clock()
font = pygame.font.Font('data/fonts/pong.ttf',48)
exit = False
button_1 = Button("row",100,100,'gray','black',4,screen,font)
button_2 = Button("column",200,100,'gray','black',4,screen,font)
while not exit:
    screen.fill((255,255,255))
    button_1.add_button(10,10)
    button_2.add_button(10,125)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                exit = True
        if event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_r] and keys[pygame.K_LSHIFT]:
                  button_2.un_press()
                  button_1.press()
            if keys[pygame.K_c] and keys[pygame.K_LSHIFT]:
                  button_1.un_press()
                  button_2.press()

    timer.tick(60)
    pygame.display.flip()