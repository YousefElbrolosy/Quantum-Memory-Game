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
    row_flag = True
    #should be unpressable unless row is selected
    col_flag = False
    #############
    exit = False
    #shuffle cards
    card_deck = CardDeck()
    card_deck.add_cards()
    shuffled_cards = card_deck.shuffle(card_deck.cards_xpics_x910)
    #text
    text_font = Text()
    button_row = Button("row    'shift+r'",325,50,'gray','black',4,screen,text_font.font)
    button_column = Button("column 'shift+c'",325,50,'gray','black',4,screen,text_font.font)
    while not exit:
        screen.fill((0,0,0))
        screen.blit(bgImg,(0,0))
        screen.blit(bgImg,(683,0))
        
        text_display = Text()

        button_row.add_button(1025,10)
        button_column.add_button(1025,60)
        if row_flag:
            button_column.un_press()
        
        #update game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = True
            elif event.type == pygame.KEYDOWN:
                circuit_grid_3.handle_input(event.key)
                circuit_grid_2.handle_input(event.key)
                keys = pygame.key.get_pressed()
                if keys[pygame.K_r] and keys[pygame.K_LSHIFT]:
                    button_column.un_press()
                    button_row.press()
                    row_flag =True
                    col_flag = False
                if keys[pygame.K_c] and keys[pygame.K_LSHIFT]:
                    button_row.un_press()
                    button_column.press()
                    col_flag = True
                    row_flag = False
            
        #display cards
        card_deck.display(352.4214876,38,shuffled_cards,screen)
        card_deck.reset8()
        text_display.reset()
        global tmpi
        global tmpj
        tmpj = 0
        #draw
        #row control (add sounds later)
        #this can be written using a for loop but I prefer not to
        if row_flag == True:
            circuit_grid_2.draw(screen)
            quantum_control_2 = Quantum_control(circuit_grid_2)
            bra_ket = quantum_control_2.select_row() 
            if bra_ket == "|00>":
                tmpi = 0
                text_display.color_list_2[tmpi] = (0,255,255)
                text_display.color_list_3[tmpj] = (0,255,255)
                card_deck.add_border(tmpi,tmpj)
            elif bra_ket == "|01>":
                tmpi = 1
                text_display.color_list_2[tmpi] = (0,255,255)
                text_display.color_list_3[tmpj] = (0,255,255)
                card_deck.add_border(tmpi,tmpj)
            elif bra_ket == "|10>":
                tmpi = 2
                text_display.color_list_2[tmpi] = (0,255,255)
                text_display.color_list_3[tmpj] = (0,255,255)
                card_deck.add_border(tmpi,tmpj)
            elif bra_ket == "|11>":
                tmpi = 3
                text_display.color_list_2[tmpi] = (0,255,255)
                text_display.color_list_3[tmpj] = (0,255,255)
                card_deck.add_border(tmpi,tmpj)
        elif col_flag == True:
            circuit_grid_3.draw(screen)
            quantum_control_3 = Quantum_control(circuit_grid_3)
            bra_ket = quantum_control_3.select_column()
            if bra_ket == "|000>":
                tmpj = 0
                text_display.color_list_2[tmpi] = (0,255,255)
                text_display.color_list_3[tmpj] = (0,255,255)
                card_deck.add_border(tmpi,tmpj)
            elif bra_ket == "|001>":
                tmpj = 1
                text_display.color_list_2[tmpi] = (0,255,255)
                text_display.color_list_3[tmpj] = (0,255,255)
                card_deck.add_border(tmpi,tmpj)
            elif bra_ket == "|010>":
                tmpj = 2
                text_display.color_list_2[tmpi] = (0,255,255)
                text_display.color_list_3[tmpj] = (0,255,255)
                card_deck.add_border(tmpi,tmpj)
            elif bra_ket == "|011>":
                tmpj = 3
                text_display.color_list_2[tmpi] = (0,255,255)
                text_display.color_list_3[tmpj] = (0,255,255)
                card_deck.add_border(tmpi,tmpj)
            elif bra_ket == "|100>":
                tmpj = 4
                text_display.color_list_2[tmpi] = (0,255,255)
                text_display.color_list_3[tmpj] = (0,255,255)
                card_deck.add_border(tmpi,tmpj)
            elif bra_ket == "|101>":
                tmpj = 5
                text_display.color_list_2[tmpi] = (0,255,255)
                text_display.color_list_3[tmpj] = (0,255,255)
                card_deck.add_border(tmpi,tmpj)
            elif bra_ket == "|110>":
                tmpj = 6
                text_display.color_list_2[tmpi] = (0,255,255)
                text_display.color_list_3[tmpj] = (0,255,255)
                card_deck.add_border(tmpi,tmpj)
            elif bra_ket == "|111>":
                tmpj = 7
                text_display.color_list_2[tmpi] = (0,255,255)
                text_display.color_list_3[tmpj] = (0,255,255)
                card_deck.add_border(tmpi,tmpj)
        
        
        text_display.display_grid(screen)
        pygame.display.flip()

        #set framerate
        clock.tick(60)

if __name__ == '__main__':
    main()