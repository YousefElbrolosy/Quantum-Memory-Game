import pygame
from controls.circuit_grid import CircuitGrid
from model.circuit_grid_model import CircuitGridModel
import tabletop
pygame.init()
#my aspect ratio is 1366 by 768
screen = pygame.display.set_mode((1366,725))
pygame.display.set_caption('Quantum Memory')
clock = pygame.time.Clock()

def main():
    #initialise game 
    circuit_grid_model = CircuitGridModel(3,19)
    circuit_grid = CircuitGrid(0,475,circuit_grid_model)
    #display cards

    exit = False
    shuffled_cards = tabletop.shuffle(tabletop.cards)
    while not exit:
        screen.fill((100,255,100))
        #update game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = True
            elif event.type == pygame.KEYDOWN:
                circuit_grid.handle_input(event.key)

        #add cards
        
        tabletop.display(10,10,shuffled_cards)

        #draw
        circuit_grid.draw(screen)
        pygame.display.flip()

        #set framerate
        clock.tick(60)

if __name__ == '__main__':
    main()