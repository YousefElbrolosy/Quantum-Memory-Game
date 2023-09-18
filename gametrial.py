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
    
    exit = False
    cheatflag = False
    #shuffle cards
    card_deck = CardDeck()
    card_deck.add_cards()
    card_deck.shuffle(card_deck.cards_xpics_x910)
    #text
    text_font = Text()
    button_row = Button("row    'shift+r'",325,50,'gray','black',4,screen,text_font.font)
    button_column = Button("column 'shift+c'",325,50,'gray','black',4,screen,text_font.font)
    #button_enter = Button("select 'enter'",325,50,'gray','black',4,screen,text_font.font)
    # button
    row_flag = True
    #should be unpressable unless row is selected
    col_flag = False
    #############
    while not exit:
        screen.fill((0,0,0))
        screen.blit(bgImg,(0,0))
        screen.blit(bgImg,(683,0))
        
        text_display = Text()

        button_row.add_button(1025,10)
        button_column.add_button(1025,60)
        #button_enter.add_button(10,10)
        #button_enter.un_press()
        global tmpi
        global tmpj
        if row_flag:
            button_column.un_press()
        
        #update game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = True
            elif event.type == pygame.KEYDOWN:
                if row_flag and not col_flag:
                    circuit_grid_2.handle_input(event.key)
                if col_flag and not row_flag:
                    circuit_grid_3.handle_input(event.key)
                keys = pygame.key.get_pressed()
                
                if keys[pygame.K_r] and (keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]):
                    button_column.un_press()
                    button_row.press()
                    row_flag =True
                    col_flag = False
                    
                if keys[pygame.K_c] and (keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]):
                    button_row.un_press()
                    button_column.press()
                    col_flag = True
                    row_flag = False
                
                if event.key == pygame.K_RETURN and button_column.pressed:
                    if not card_deck.no_border:
                        card_deck.flip(tmpi,tmpj)
                        #button_enter.press()
                        button_row.press()
                        button_column.un_press()
                        row_flag = True
                        col_flag = False
                        circuit_grid_model_3 = CircuitGridModel(3,19)
                        circuit_grid_3 = CircuitGrid(0,518,circuit_grid_model_3)
                        circuit_grid_model_2 = CircuitGridModel(2,19)  
                        circuit_grid_2 = CircuitGrid(0,575,circuit_grid_model_2)
                elif keys[pygame.K_q]:
                    cheatflag = True
                elif keys[pygame.K_r]:
                    cheatflag = False
                    
                    
                    
                    
            
        #display cards
        #card_deck.display(352.4214876,38,shuffled_cards,screen)
        if cheatflag:
            card_deck.cheat_dict(352.4214876,38,screen)
        else:
            card_deck.display_dict(352.4214876,38,screen)
        card_deck.reset8()
        text_display.reset()
        print(list(card_deck.flip_dictionary))
        
        if len(card_deck.flip_dictionary) == 2:
            #time.sleep(1)
            card_deck.check_cards()
        
        tmpj = 0
        #draw
        #row control (add sounds later)
        #this can be written using a for loop but I prefer not to
        if row_flag == True and col_flag == False:
            circuit_grid_2.draw(screen)
            quantum_control_2 = Quantum_control(circuit_grid_2)
            bra_ket_2 = quantum_control_2.select_row() 
            if bra_ket_2 == "|00>":
                tmpi = 0
                if not card_deck.no_border:
                    text_display.color_list_2[tmpi] = (0,255,255)
                    text_display.color_list_3[tmpj] = (0,255,255)
                card_deck.add_border(tmpi,tmpj)
            elif bra_ket_2 == "|01>":
                tmpi = 1
                if not card_deck.no_border:
                    text_display.color_list_2[tmpi] = (0,255,255)
                    text_display.color_list_3[tmpj] = (0,255,255)
                card_deck.add_border(tmpi,tmpj)
            elif bra_ket_2 == "|10>":
                tmpi = 2
                if not card_deck.no_border:
                    text_display.color_list_2[tmpi] = (0,255,255)
                    text_display.color_list_3[tmpj] = (0,255,255)
                card_deck.add_border(tmpi,tmpj)
            elif bra_ket_2 == "|11>":
                tmpi = 3
                if not card_deck.no_border:
                    text_display.color_list_2[tmpi] = (0,255,255)
                    text_display.color_list_3[tmpj] = (0,255,255)
                card_deck.add_border(tmpi,tmpj)
        elif col_flag == True and row_flag == False:
            circuit_grid_3.draw(screen)
            quantum_control_3 = Quantum_control(circuit_grid_3)
            bra_ket_3 = quantum_control_3.select_column()
            if bra_ket_3 == "|000>":
                tmpj = 0
                if not card_deck.no_border:
                    text_display.color_list_2[tmpi] = (0,255,255)
                    text_display.color_list_3[tmpj] = (0,255,255)
                card_deck.add_border(tmpi,tmpj)
            elif bra_ket_3 == "|001>":
                tmpj = 1
                if not card_deck.no_border:
                    text_display.color_list_2[tmpi] = (0,255,255)
                    text_display.color_list_3[tmpj] = (0,255,255)
                card_deck.add_border(tmpi,tmpj)
            elif bra_ket_3 == "|010>":
                tmpj = 2
                if not card_deck.no_border:
                    text_display.color_list_2[tmpi] = (0,255,255)
                    text_display.color_list_3[tmpj] = (0,255,255)
                card_deck.add_border(tmpi,tmpj)
            elif bra_ket_3 == "|011>":
                tmpj = 3
                if not card_deck.no_border:
                    text_display.color_list_2[tmpi] = (0,255,255)
                    text_display.color_list_3[tmpj] = (0,255,255)
                card_deck.add_border(tmpi,tmpj)
            elif bra_ket_3 == "|100>":
                tmpj = 4
                if not card_deck.no_border:
                    text_display.color_list_2[tmpi] = (0,255,255)
                    text_display.color_list_3[tmpj] = (0,255,255)
                card_deck.add_border(tmpi,tmpj)
            elif bra_ket_3 == "|101>":
                tmpj = 5
                if not card_deck.no_border:
                    text_display.color_list_2[tmpi] = (0,255,255)
                    text_display.color_list_3[tmpj] = (0,255,255)
                card_deck.add_border(tmpi,tmpj)
            elif bra_ket_3 == "|110>":
                tmpj = 6
                if not card_deck.no_border:
                    text_display.color_list_2[tmpi] = (0,255,255)
                    text_display.color_list_3[tmpj] = (0,255,255)
                card_deck.add_border(tmpi,tmpj)
            elif bra_ket_3 == "|111>":
                tmpj = 7
                if not card_deck.no_border:
                    text_display.color_list_2[tmpi] = (0,255,255)
                    text_display.color_list_3[tmpj] = (0,255,255)
                card_deck.add_border(tmpi,tmpj)
        
        
        text_display.display_grid(screen)
        pygame.display.flip()

        #set framerate
        clock.tick(60)

if __name__ == '__main__':
    main()