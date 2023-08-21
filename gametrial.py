import pygame
from controls.circuit_grid import CircuitGrid
from model.circuit_grid_model import CircuitGridModel
pygame.init()
screen = pygame.display.set_mode((1185,700))
pygame.display.set_caption('Brolos')
clock = pygame.time.Clock()

def main():
    #initialise game 
    circuit_grid_model = CircuitGridModel(3,16)
    circuit_grid = CircuitGrid(0,475,circuit_grid_model)


    exit = False
    while not exit:
        #update game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = True
            elif event.type == pygame.KEYDOWN:
                circuit_grid.handle_input(event.key)       

        #draw
        circuit_grid.draw(screen)
        pygame.display.flip()

        #set framerate
        clock.tick(60)

if __name__ == '__main__':
    main()