import pygame
from controls.circuit_grid import CircuitGrid
from model.circuit_grid_model import CircuitGridModel
from quantum import Quantum_control
from card_deck import CardDeck
from text_display import Text
pygame.init()
#my aspect ratio is 1366 by 768
screen = pygame.display.set_mode((1366,768))
pygame.display.set_caption('Quantum Memory')
clock = pygame.time.Clock()
bgImg = pygame.image.load('data/photos/space.jpg')
default_text_color = (255,255,255)
def main():
    #initialise game 
    circuit_grid_model_3 = CircuitGridModel(3,19)
    circuit_grid_3 = CircuitGrid(0,518,circuit_grid_model_3)
    circuit_grid_model_2 = CircuitGridModel(2,19)  
    circuit_grid_2 = CircuitGrid(0,575,circuit_grid_model_2)
    # should be made ito a button
    row_flag = True
    #should be unpressable unless row is selected
    col_flag = False
    #############
    exit = False
    #shuffle cards
    card_deck = CardDeck()
    card_deck.add_cards()
    shuffled_cards = card_deck.shuffle(card_deck.cards_xpics_x910)
    while not exit:
        screen.fill((0,0,0))
        screen.blit(bgImg,(0,0))
        screen.blit(bgImg,(683,0))
        #update game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = True
            elif event.type == pygame.KEYDOWN:
                circuit_grid_3.handle_input(event.key)
                circuit_grid_2.handle_input(event.key)

        
        #display cards
        card_deck.display(352.4214876,38,shuffled_cards,screen)
        card_deck.reset8()
        #text
        text_display = Text()
        #works in updating the cursor but leads to a memory expensive for loop
        text_display.reset()
        #draw
        #row control (add sounds later)
        #this can be written using a for loop but I prefer not to
        if row_flag == True:
            circuit_grid_2.draw(screen)
            quantum_control = Quantum_control(circuit_grid_2)
            bra_ket = quantum_control.select_row() 
            if bra_ket == "|00>":
                text_display.color_list_2[0] = (0,255,255)
                card_deck.add_border(0,0)
            elif bra_ket == "|01>":
                text_display.color_list_2[1] = (0,255,255)
                card_deck.add_border(1,0)
            elif bra_ket == "|10>":
                text_display.color_list_2[2] = (0,255,255)
                card_deck.add_border(2,0)
            elif bra_ket == "|11>":
                text_display.color_list_2[3] = (0,255,255)
                card_deck.add_border(3,0)
        elif col_flag == True:
            circuit_grid_3.draw(screen)
            quantum_control = Quantum_control(circuit_grid_3)
            bra_ket = quantum_control.select_column()
            if bra_ket == "|000>":
                text_display.color_list_3[0] = (0,255,255)
            elif bra_ket == "|001>":
                text_display.color_list_3[1] = (0,255,255)
            elif bra_ket == "|010>":
                text_display.color_list_3[2] = (0,255,255)
            elif bra_ket == "|011>":
                text_display.color_list_3[3] = (0,255,255)
            elif bra_ket == "|100>":
                text_display.color_list_3[4] = (0,255,255)
            elif bra_ket == "|101>":
                text_display.color_list_3[5] = (0,255,255)
            elif bra_ket == "|110>":
                text_display.color_list_3[6] = (0,255,255)
            elif bra_ket == "|111>":
                text_display.color_list_3[7] = (0,255,255)
        
        
        text_display.display_grid(screen)
        pygame.display.flip()

        #set framerate
        clock.tick(60)

if __name__ == '__main__':
    main()