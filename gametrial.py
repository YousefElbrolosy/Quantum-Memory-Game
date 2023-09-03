import pygame
from controls.circuit_grid import CircuitGrid
from model.circuit_grid_model import CircuitGridModel
from quantum import Quantum_control
from card_deck import CardDeck
from text_display import Text
from button import Button
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
    row_flag = False
    #should be unpressable unless row is selected
    col_flag = True
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
        #text
        text_display = Text()
        row_button = Button("Row", 100, 100 ,10 ,10,screen,text_display.font)
        col_button = Button("Column", 200 ,100 ,10 ,150,screen,text_display.font)
        #update game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = True
            elif event.type == pygame.KEYDOWN:
                circuit_grid_3.handle_input(event.key)
                circuit_grid_2.handle_input(event.key)
                if (event.key == pygame.K_LSHIFT):
                    col_button.pressed = True
                    col_flag = True
                    row_button.enabled = False
                elif (event.key == pygame.K_RSHIFT):
                    row_button.pressed = True
                    print("pressed succ")
                    row_flag = True
                    col_button.enabled = False
            
        #display cards
        card_deck.display(352.4214876,38,shuffled_cards,screen)
        card_deck.reset8()
        
        #works in updating the cursor but leads to a memory expensive for loop
        text_display.reset()
        global tmpi
        global tmpj
        tmpi = 0
        #draw
        #row control (add sounds later)
        #this can be written using a for loop but I prefer not to
        if row_flag == True:
            circuit_grid_2.draw(screen)
            quantum_control = Quantum_control(circuit_grid_2)
            bra_ket = quantum_control.select_row() 
            if bra_ket == "|00>":
                tmpi = 0
                text_display.color_list_2[tmpi] = (0,255,255)
                card_deck.add_border(tmpi,tmpj)
            elif bra_ket == "|01>":
                tmpi = 1
                text_display.color_list_2[tmpi] = (0,255,255)
                card_deck.add_border(tmpi,tmpj)
            elif bra_ket == "|10>":
                tmpi = 2
                text_display.color_list_2[tmpi] = (0,255,255)
                card_deck.add_border(tmpi,tmpj)
            elif bra_ket == "|11>":
                tmpi = 3
                text_display.color_list_2[tmpi] = (0,255,255)
                card_deck.add_border(tmpi,tmpj)
        elif col_flag == True:
            circuit_grid_3.draw(screen)
            quantum_control = Quantum_control(circuit_grid_3)
            bra_ket = quantum_control.select_column()
            if bra_ket == "|000>":
                tmpj = 0
                text_display.color_list_3[tmpj] = (0,255,255)
                card_deck.add_border(tmpi,tmpj)
            elif bra_ket == "|001>":
                tmpj = 1
                text_display.color_list_3[tmpj] = (0,255,255)
                card_deck.add_border(tmpi,tmpj)
            elif bra_ket == "|010>":
                tmpj = 2
                text_display.color_list_3[tmpj] = (0,255,255)
                card_deck.add_border(tmpi,tmpj)
            elif bra_ket == "|011>":
                tmpj = 3
                text_display.color_list_3[tmpj] = (0,255,255)
                card_deck.add_border(tmpi,tmpj)
            elif bra_ket == "|100>":
                tmpj = 4
                text_display.color_list_3[tmpj] = (0,255,255)
                card_deck.add_border(tmpi,tmpj)
            elif bra_ket == "|101>":
                tmpj = 5
                text_display.color_list_3[tmpj] = (0,255,255)
                card_deck.add_border(tmpi,tmpj)
            elif bra_ket == "|110>":
                tmpj = 6
                text_display.color_list_3[tmpj] = (0,255,255)
                card_deck.add_border(tmpi,tmpj)
            elif bra_ket == "|111>":
                tmpj = 7
                text_display.color_list_3[tmpj] = (0,255,255)
                card_deck.add_border(tmpi,tmpj)
        
        
        text_display.display_grid(screen)
        pygame.display.flip()

        #set framerate
        clock.tick(60)

if __name__ == '__main__':
    main()