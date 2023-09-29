from button import Button
import pygame
import operator
import card_deck
import random
pygame.init()
screen = pygame.display.set_mode((500,500))
fps = 60
timer = pygame.time.Clock()
font = pygame.font.Font('data/fonts/pong.ttf',48)
exit = False
button_1 = Button("row",100,100,'gray','black',4,screen,font)
button_2 = Button("column",200,100,'gray','black',4,screen,font)

def main():
    x = [(0, 0), (3, 0), (0, 1), (3, 1), (0, 6), (3, 6), (0, 7), (3, 7)]
    #[[(0,0),(0,1),(0,6),(0,7)],
    #        [(3,0),(3,1),(3,6),(3,7)]]
    #y = sorted(x, key= operator.itemgetter(0))
    z = sorted(x, key = lambda x: x[0])
    tmp = z[0][0]
    matrix = [[]]
    k = 0
    for (i,j) in z:
        if i == tmp:
            matrix[k].append((i,j))
        else:
            matrix.append([])
            k+=1
            matrix[k].append((i,j))
            tmp = i
    matrix1 = [[(0,1),(0,6),(0,7)],
                [(3,0),(3,1),(3,6)]]
    super_prob_2 = [(0.4999999999999999), (0.4999999999999999)]
    super_prob_3 = [(0.2499999999999999), (0.2499999999999999), (0.2499999999999999), (0.2499999999999999)]
    
    row_measurement = random.choices(matrix1,weights= super_prob_2, k = 1)
    print(row_measurement)
    col_measurement = random.choices(list(row_measurement[0]), weights = super_prob_3, k = 1)
    print(col_measurement)
    
               

if __name__ == '__main__':
    main()
"""          
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
"""