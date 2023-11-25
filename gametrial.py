import pygame
from controls.circuit_grid import CircuitGrid
from model.circuit_grid_model import CircuitGridModel
from quantum import Quantum_control
from card_deck import CardDeck
from text_display import Text
from button import Button
from pygame import mixer
import time
pygame.init()
mixer.music.load('data/music/gameplay.wav')
mixer.music.set_volume(0.88)
mixer.music.play(-1)
#my aspect ratio is 1366 by 768
card_deck = CardDeck()
screen = pygame.display.set_mode((1366,768))
pygame.display.set_caption('Quantum Memory')
clock = pygame.time.Clock()
bgImg = pygame.image.load('utils/data/images/Space-Background-Images.jpg')
bgImg_start = pygame.transform.scale(pygame.image.load('data/photos/Space-Background-Image-2.jpg'),(1366,768))
select_sound = mixer.Sound('data/music/change_selection.wav')
select_sound.set_volume(0.1)


#Background sound

default_text_color = (255,255,255)
transition_to_noise = False
high_score_zero = 0
best_attempt = 0
button_chosen = 0
button_chosen_1 = 0
class StartScreen():
    exit = False
    global select_sound
    def __init__(self):
        self.transition_to_start = True
        self.transition = False
        self.transition_to_options = False
        self.transition_to_end = False
        self.restart = False
    def start_screen(self):
        global transition_to_noise

        text_font = Text()
        screen.fill((0,0,0))
        screen.blit(bgImg_start,(0,0))
        text = text_font.font_title.render("WELCOME TO",True,'gold')
        text_2 = text_font.font_title.render("QUANTUM MEMORY",True,'gold')
        text_border = text_font.font_title_border.render("WELCOME TO",True,'black')
        text_border_2 = text_font.font_title_border.render("QUANTUM MEMORY",True,'black')
        screen.blit(text_border,(375,150))
        screen.blit(text_border_2,(250,280))
        screen.blit(text,(375,150))
        screen.blit(text_2,(250,280))

        button_easy = Button("Play without noise",375,75,'gray','black','black',4,screen,text_font.font)

        button_enter_noise = Button("play with noise",375,75,'gray','black','black',4,screen,text_font.font)
        button_options = Button("How to play",375,75,'gray','black','black',4,screen,text_font.font)
        button_exit = Button("exit",375,75,'gray','black','black',4,screen,text_font.font)
        global button_chosen

        if button_chosen == 0:
            button_easy.press()
            button_enter_noise.un_press()
            button_options.un_press()
            button_exit.un_press()
        if button_chosen == 1:
            button_easy.un_press()
            button_enter_noise.press()
            button_options.un_press()
            button_exit.un_press()
        if button_chosen == 2:
            button_easy.un_press()
            button_enter_noise.un_press()
            button_options.press()
            button_exit.un_press()
        if button_chosen == 3:
            button_easy.un_press()
            button_enter_noise.un_press()
            button_options.un_press()
            button_exit.press()

        button_easy.add_button((1366/2)-400,(768/3)+175)
        
        button_enter_noise.add_button((1366/2),(768/3)+175)
        
        button_options.add_button(((1366/2))-400,(768/3)+300)

        button_exit.add_button((1366/2),(768/3)+300)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.exit = True
            elif event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if event.key == pygame.K_RIGHT and button_chosen !=3 :
                    button_chosen = button_chosen + 1
                    select_sound.play()
                   
                if event.key == pygame.K_LEFT and button_chosen !=0 :
                    button_chosen-=1
                    select_sound.play()
                    
                if event.key == pygame.K_UP and button_chosen == 2 :
                    button_chosen = 0
                    select_sound.play()
                    
                if event.key == pygame.K_UP and button_chosen == 3 :
                    button_chosen = 1
                    select_sound.play()
                    
                if event.key == pygame.K_DOWN and button_chosen == 0 :
                    button_chosen = 2
                    select_sound.play()
                   
                if event.key == pygame.K_DOWN and button_chosen == 1 :
                    button_chosen = 3
                    select_sound.play()
                    
                if event.key == pygame.K_RETURN:
                    select_sound.play()
                    if event.key == pygame.K_RETURN and button_chosen == 0:
                        self.transition = True
                        transition_to_noise = False
                        self.transition_to_start = False
                        button_easy.press()
                        mixer.music.set_volume(0.5)
                        
                        
                    if event.key == pygame.K_RETURN and button_chosen == 1:
                        self.transition = True
                        transition_to_noise = True
                        self.transition_to_start = False
                        button_enter_noise.press() 
                    if event.key == pygame.K_RETURN and button_chosen == 2 :
                        self.transition_to_options = True
                        self.transition = False
                        self.transition_to_start = False
                        self.settings_screen()
                    if event.key == pygame.K_RETURN and button_chosen == 3:
                        time.sleep(0.2)
                        self.exit = True
        pygame.display.flip()

    def settings_screen(self):
        screen.fill((0,0,0))
        screen.blit(bgImg_start,(0,0))
        text_font = Text()
        button_back = Button("     back 'b'",375,75,'gray','black','black',4,screen,text_font.font)
        button_back.add_button(((1366/2) - (375/2)),((768/2)+175))
        game_controls_txt = text_font.font_subtitle.render("Game Controls",True,'gold')
        game_controls_border = text_font.font_subtitle_border.render("Game Controls",True,'black')
        wasd_text = text_font.small_font.render("Cursor Movement", True, (0,255,255))
        wasd_text_border = text_font.small_font_border.render("Cursor Movement", True, (0,0,0))
        h_text = text_font.small_font.render("Hadamard Gate: puts the qubit into", True, (0,255,255))
        h_text_2 = text_font.small_font.render("an equal superpositon of |0> and |1>", True, (0,255,255))
        h_text_border = text_font.small_font_border.render("Hadamard Gate: puts the qubit into", True, (0,0,0))
        h_text_border_2 = text_font.small_font_border.render("an equal superpositon of |0> and |1>", True, (0,0,0))
        x_text = text_font.small_font.render("the Not Gate: flips the state of the", True, (0,255,255))
        x_text_2 = text_font.small_font.render("qubit from |0> to |1> and vice versa", True, (0,255,255))
        x_text_border = text_font.small_font_border.render("the Not Gate: flips the state of the", True, (0,0,0))
        x_text_border_2 = text_font.small_font_border.render("qubit from |0> to |1> and vice versa", True, (0,0,0))
        
        screen.blit(wasd_text_border,(802,170))
        screen.blit(wasd_text,(805,170))
        screen.blit(h_text_border,(722,295))
        screen.blit(h_text_border_2,(722,325))
        screen.blit(h_text,(725,295))
        screen.blit(h_text_2,(725,325))
        screen.blit(x_text_border,(722,400))
        screen.blit(x_text_border_2,(722,430))
        screen.blit(x_text,(725,400))
        screen.blit(x_text_2,(725,430))
        screen.blit(game_controls_border,(775,50))
        screen.blit(game_controls_txt,(775,50))
        h_gate = pygame.image.load('utils/data/gate_images/h_gate.png')
        x_gate = pygame.image.load('utils/data/gate_images/x_gate.png')
        id_gate = pygame.image.load('utils/data/gate_images/iden_gate.png')
        cursor = pygame.transform.scale(pygame.image.load('utils/data/images/circuit-grid-cursor.png'),(33,33))
        wasd = pygame.transform.scale(pygame.image.load('data/photos/wasd5.png'),(200,200))
        screen.blit(wasd,(585,100))
        screen.blit(h_gate,(655,300))
        screen.blit(x_gate,(655,405))
        #screen.blit(id_gate,(655,450))
        screen.blit(cursor,(1175,195))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.exit = True
            elif event.type == pygame.KEYDOWN:
                #back button
                if event.key == pygame.K_b:
                    select_sound.play()
                    self.transition_to_options = False

    def end_screen(self):
        global card_deck
        screen.fill((0,0,0))
        screen.blit(bgImg_start,(0,0))
        text_font = Text()
        congratulations = text_font.font_title.render("CONGRATULATIONS",True,'gold')
        you_have = text_font.font_title.render("YOU NOW HAVE A",True,'gold')
        quantum_memory = text_font.font_title.render("QUANTUM MEMORY",True,'gold')
        congratulations_border = text_font.font_title_border.render("CONGRATULATIONS",True,'black')
        you_have_border = text_font.font_title_border.render("YOU NOW HAVE A",True,'black')
        quantum_memory_border = text_font.font_title.render("QUANTUM MEMORY",True,'black')
        screen.blit(congratulations_border,(200,125))
        screen.blit(you_have_border,(225,255))
        screen.blit(quantum_memory_border,(255,385))
        screen.blit(congratulations,(200,125))
        screen.blit(you_have,(225,255))
        screen.blit(quantum_memory,(250,385))

        
        score = text_font.font_subtitle.render("Your Score is:" + str(card_deck.score),True,(0,255,255))
        score_border = text_font.font_subtitle_border.render("Your Score is:" + str(card_deck.score),True,'black')       
        screen.blit(score_border,(253,500))
        screen.blit(score,(250,500))
        attempts = text_font.font_subtitle.render("number of attempts: " + str(card_deck.attempts),True,(0,255,255))
        attempts_border = text_font.font_subtitle_border.render("number of attempts: " + str(card_deck.score),True,'black')       
        screen.blit(attempts_border,(253,550))
        screen.blit(attempts,(250,550))

        button_restart = Button("restart",375,75,'gray','black','black',4,screen,text_font.font)

        button_quit = Button("quit",325,75,'gray','black','black',4,screen,text_font.font)
        global button_chosen
        global high_score_zero
        global best_attempt
        if button_chosen == 0:
            button_restart.press()
            button_quit.un_press()
            
        if button_chosen == 1:
            button_restart.un_press()
            button_quit.press()
        

        button_restart.add_button((1366/2)-400,(768/2)+250)
        
        button_quit.add_button((1366/2),(768/2)+250)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.exit = True
            elif event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if event.key == pygame.K_RIGHT and button_chosen !=1 :
                    button_chosen = button_chosen + 1
                    select_sound.play()
                    
                if event.key == pygame.K_LEFT and button_chosen !=0 :
                    button_chosen-=1
                    select_sound.play()
                    
                   
                if event.key == pygame.K_RETURN and button_chosen == 0:
                    button_restart.press()
                    high_score_zero = card_deck.score
                    best_attempt = card_deck.attempts
                    self.transition = False
                    self.transition_to_start = True
                    self.transition_to_end = False
                    self.transition_to_options = False
                    self.restart = True
                if event.key == pygame.K_RETURN and button_chosen == 1:
                    button_quit.press()
                    time.sleep(0.2) 
                    self.exit = True


        pygame.display.flip()
def main():
    #initialise game 
    
    circuit_grid_model_3 = CircuitGridModel(3,19)
    circuit_grid_3 = CircuitGrid(0,518,circuit_grid_model_3)
    circuit_grid_model_2 = CircuitGridModel(2,19)  
    circuit_grid_2 = CircuitGrid(0,575,circuit_grid_model_2)
    break_flag = False
    exit = False
    cheatflag = False
    superposition_flag_2 = False
    superposition_flag_3 = False
    global revert_to_no_noise
    revert_to_no_noise = False
    super_prob_2 = []
    super_prob_3 = []
    global error_mitigate_bg_color
    global error_mitigate_text_color
    
    error_mitigate_bg_color = (50,50,50)
    tmp_color = error_mitigate_bg_color
    error_mitigate_text_color = (80,80,80)
    tmp_text_color = (80,80,80)
    #shuffle cards
    global card_deck
    card_deck.add_cards()
    card_deck.shuffle(card_deck.cards_xpics_x910)
    #text
    text_font = Text()
    button_row = Button("row    'shift+r'",333,50,'gray','black','black',4,screen,text_font.font)
    button_column = Button("column 'shift+c'",333,50,'gray','black','black',4,screen,text_font.font)
    button_h = Button("HADAMARD  'H'",333,50,tmp_color,'black',tmp_text_color,4,screen,text_font.font)
    button_x = Button("X gate    'x'",333,50,tmp_color,'black',tmp_text_color,4,screen,text_font.font)
    button_cnot = Button("CONTROL GATE+'C'",333,50,tmp_color,'black',tmp_text_color,4,screen,text_font.font)
    button_y = Button("Y GATE    'Y'",333,50,tmp_color,'black',tmp_text_color,4,screen,text_font.font)
    button_z = Button("Z gate    'Z'",333,50,tmp_color,'black',tmp_text_color,4,screen,text_font.font)
    button_rotate = Button("ROTATE '>' OR '<'",333,50,tmp_color,'black',tmp_text_color,4,screen,text_font.font)
    button_flip = Button("flip 'enter'",230,50,'gray','black','black',4,screen,text_font.font)
    button_w = Button("UP  'W'",230,50,tmp_color,'black',tmp_text_color,4,screen,text_font.font)
    button_a = Button("LEFT  'A'",230,50,tmp_color,'black',tmp_text_color,4,screen,text_font.font)
    button_s = Button("DOWN 'S'",230,50,tmp_color,'black',tmp_text_color,4,screen,text_font.font)
    button_d = Button("RIGHT 'D'",230,50,tmp_color,'black',tmp_text_color,4,screen,text_font.font)
    button_mitigate_noise = Button("ERROR MITIGATION",333,50,error_mitigate_bg_color,'black',error_mitigate_text_color,4,screen,text_font.font)
    #button_enter = Button("select 'enter'",325,50,'gray','black',4,screen,text_font.font)
    # button
    row_flag = True
    #should be unpressable unless row is selected
    col_flag = False
    #############
    first_scene = StartScreen()
    
    while not exit:
        
        exit = first_scene.exit
        if first_scene.start_screen and not first_scene.transition and not first_scene.transition_to_options and not first_scene.transition_to_end:
            first_scene.start_screen()
        elif first_scene.transition_to_options and not first_scene.transition:
            first_scene.settings_screen()
        
        elif first_scene.transition:
            screen.fill((0,0,0))
            screen.blit(pygame.transform.scale(bgImg,(1366,768)),(0,0))
            
            score = text_font.small_font_border.render("Score: "+str(card_deck.score),True,'dark gray')
            screen.blit(score,(10,80))      
            high_score = text_font.small_font_border.render("High Score: "+str(high_score_zero),True,'dark gray')
            best_attempt_text = text_font.small_font_border.render("BEST Number",True,'dark gray')
            best_attempt_text_2 = text_font.small_font_border.render("OF attempts",True,'dark gray')
            best_attempt_text_3 = text_font.small_font_border.render(":"+str(best_attempt),True,'dark gray')
            screen.blit(high_score,(10,130))  
            screen.blit(best_attempt_text,(10,180))
            screen.blit(best_attempt_text_2,(10,210))
            screen.blit(best_attempt_text_3,(200,195))
            text_display = Text()
            button_row.add_button(1025,10)
            button_column.add_button(1025,65)
            button_flip.add_button(5,10)
            button_w.add_button(5,260)
            button_s.add_button(5,315)
            button_d.add_button(5,370)
            button_a.add_button(5,425)
            button_h.add_button(1025,120)
            button_x.add_button(1025,175)
            button_y.add_button(1025,230)
            button_z.add_button(1025,285)
            button_cnot.add_button(1025,340)
            button_rotate.add_button(1025,395)
            if transition_to_noise:
                button_mitigate_noise.add_button(1025,450)
            button_h.un_press()
            button_x.un_press()
            button_y.un_press()
            button_z.un_press()
            button_w.un_press()
            button_a.un_press()
            button_s.un_press()
            button_d.un_press()
            button_cnot.un_press()
            button_rotate.un_press()
            button_mitigate_noise.un_press()

            if card_deck.score >= 15:
                button_mitigate_noise.press()
                button_mitigate_noise.set_txt_color((0,100,100)) 
                button_mitigate_noise.set_color('gray')
                button_mitigate_noise.set_border_color((0,150,150))
                revert_to_no_noise = True
            #button_enter.add_button(10,10)
            #button_enter.un_press()
            global tmpi
            global tmpj
            global tmp_2_state_vector_2
            global tmp_2_state_vector_3
            global tmp_1_state_vector_2
            global tmp_1_state_vector_3
            

            if row_flag:
                
                button_column.un_press()
                button_flip.un_press()
            
            #update game
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit = True
                elif event.type == pygame.KEYDOWN:
                    keys = pygame.key.get_pressed()
                    if row_flag and not col_flag and len(card_deck.flip_dictionary) < 2:
                        circuit_grid_2.handle_input(event.key)
                    if col_flag and not row_flag and len(card_deck.flip_dictionary) < 2:
                        circuit_grid_3.handle_input(event.key)
                    
                    
                    if keys[pygame.K_r] and (keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]):
                        if col_flag == True:
                            button_column.un_press()
                            button_row.press()
                            row_flag =True
                            col_flag = False
                        
                    if keys[pygame.K_c] and (keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]) and len(card_deck.flip_dictionary) < 2:
                        button_row.un_press()
                        button_column.press()
                        col_flag = True
                        row_flag = False

                    pygame.time.set_timer(pygame.K_RETURN,1000) 
                    
                    if event.key == pygame.K_RETURN and button_column.pressed:
                        #print(state_vector_2,state_vector_3)
                        #print("---")
                        
                        button_flip.press()
                        time.sleep(0.025)
                        if not card_deck.no_border:
                            card_deck.flip(super_prob_2, super_prob_3,transition_to_noise, revert_to_no_noise)
                            #button_enter.press()
                            if len(card_deck.flip_dictionary) == 1:
                        # note that it is evennt.type not event.key
                                tmp_1_state_vector_2 = state_vector_2
                                tmp_1_state_vector_3 = state_vector_3
                                #print(state_vector_2,state_vector_3)
                            if len(card_deck.flip_dictionary) == 2:
                        # note that it is evennt.type not event.key
                                tmp_2_state_vector_2 = state_vector_2
                                tmp_2_state_vector_3 = state_vector_3
                                #print(state_vector_2,state_vector_3)
                            if card_deck.flipped:
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
                

            card_deck.reset6(row_flag,col_flag, superposition_flag_2, superposition_flag_3)
            text_display.reset()

             

            tmpj = 0
            #draw
            #row control (add sounds later)
            if row_flag == True and col_flag == False:
                circuit_grid_2.draw(screen)
                quantum_control_2 = Quantum_control(circuit_grid_2)
                row_states = quantum_control_2.select_row() 
                superposition_flag_2 = quantum_control_2.superpositon_flag_2
                #if superposition_flag_2:
                #    card_deck.oscillate()
                super_prob_2 = quantum_control_2.prob_2
                state_vector_2 = quantum_control_2.state_vector_2
                for i in range(len(text_display.state_list_2)):
                    for j in range(len(row_states)):
                        if row_states[j] == text_display.state_list_2[i]:
                            if not card_deck.no_border and not transition_to_noise or revert_to_no_noise:
                                text_display.color_list_3[tmpj] = (0,255,255)
                            elif not card_deck.no_border and transition_to_noise and not revert_to_no_noise:
                                text_display.color_list_3[tmpj] = (255,0,0)
                            
                            if transition_to_noise and not revert_to_no_noise:
                                text_display.color_list_2[i] = (255,0,0) 
                            else:
                                text_display.color_list_2[i] = (0,255,255) 
                            if transition_to_noise and not revert_to_no_noise:         
                                card_deck.add_border(i,tmpj,(255,0,0))
                            else:        
                                card_deck.add_border(i,tmpj,(0,255,255))
                            tmpi = i
                            

                """
                if row_states[0] == "|00>":
                    tmpi = 0
                    if not card_deck.no_border:
                        text_display.color_list_3[tmpj] = (0,255,255)
                    text_display.color_list_2[tmpi] = (0,255,255)      
                    card_deck.add_border(tmpi,tmpj)
                elif row_states[0] == "|01>":
                    tmpi = 1
                    if not card_deck.no_border:
                        text_display.color_list_3[tmpj] = (0,255,255)
                    text_display.color_list_2[tmpi] = (0,255,255)
                    card_deck.add_border(tmpi,tmpj)
                elif row_states[0] == "|10>":
                    tmpi = 2
                    if not card_deck.no_border:
                        text_display.color_list_3[tmpj] = (0,255,255)
                    text_display.color_list_2[tmpi] = (0,255,255)
                    card_deck.add_border(tmpi,tmpj)
                elif row_states[0] == "|11>":
                    tmpi = 3
                    if not card_deck.no_border:
                        text_display.color_list_3[tmpj] = (0,255,255)
                    text_display.color_list_2[tmpi] = (0,255,255)
                    card_deck.add_border(tmpi,tmpj)
                """
            
            elif col_flag == True and row_flag == False:
                circuit_grid_3.draw(screen)
                quantum_control_3 = Quantum_control(circuit_grid_3)
                col_states = quantum_control_3.select_column()
                superposition_flag_3 = quantum_control_3.superpositon_flag_3
                #if superposition_flag_3:
                #    card_deck.oscillate()
                super_prob_3 = quantum_control_3.prob_3
                state_vector_3 = quantum_control_3.state_vector_3
                for j in range(len(text_display.state_list_3)):
                    for row_state in (row_states):
                        if row_state == "|00>":
                            i = 0
                        elif row_state == "|01>":
                            i = 1
                        elif row_state == "|10>":
                            i = 2
                        elif row_state == "|11>":
                            i = 3
                        for k in range(len(col_states)):
                            if col_states[k] == text_display.state_list_3[j]:
                                if transition_to_noise and not revert_to_no_noise:
                                    text_display.color_list_2[i] = (255,0,0)
                                    #if not card_deck.no_border:
                                    text_display.color_list_3[j] = (255,0,0)
                                    card_deck.add_border(i,j,(255,0,0))
                                else:    
                                    text_display.color_list_2[i] = (0,255,255)
                                    #if not card_deck.no_border:
                                    text_display.color_list_3[j] = (0,255,255)
                                    card_deck.add_border(i,j,(0,255,255))
                                
                                tmpj = j
                                
                            #break_flag = True
                            #break
                    #if break_flag:
                        #break_flag = False
                        #break
                """
                if col_states[0] == "|000>":
                    tmpj = 0
                    text_display.color_list_2[tmpi] = (0,255,255)
                    if not card_deck.no_border:
                        text_display.color_list_3[tmpj] = (0,255,255)
                    card_deck.add_border(tmpi,tmpj)
                elif col_states[0] == "|001>":
                    tmpj = 1
                    text_display.color_list_2[tmpi] = (0,255,255)
                    if not card_deck.no_border:
                        text_display.color_list_3[tmpj] = (0,255,255)
                    card_deck.add_border(tmpi,tmpj)
                elif col_states[0] == "|010>":
                    tmpj = 2
                    text_display.color_list_2[tmpi] = (0,255,255)
                    if not card_deck.no_border:
                        text_display.color_list_3[tmpj] = (0,255,255)
                    card_deck.add_border(tmpi,tmpj)
                elif col_states[0] == "|011>":
                    tmpj = 3
                    text_display.color_list_2[tmpi] = (0,255,255)
                    if not card_deck.no_border: 
                        text_display.color_list_3[tmpj] = (0,255,255)
                    card_deck.add_border(tmpi,tmpj)
                elif col_states[0] == "|100>":
                    tmpj = 4
                    text_display.color_list_2[tmpi] = (0,255,255)
                    if not card_deck.no_border:  
                        text_display.color_list_3[tmpj] = (0,255,255)
                    card_deck.add_border(tmpi,tmpj)
                elif col_states[0] == "|101>":
                    tmpj = 5
                    text_display.color_list_2[tmpi] = (0,255,255)
                    if not card_deck.no_border:       
                        text_display.color_list_3[tmpj] = (0,255,255)
                    card_deck.add_border(tmpi,tmpj)
                elif col_states[0] == "|110>":
                    tmpj = 6
                    text_display.color_list_2[tmpi] = (0,255,255)
                    if not card_deck.no_border:
                        text_display.color_list_3[tmpj] = (0,255,255)
                    card_deck.add_border(tmpi,tmpj)
                elif col_states[0] == "|111>":
                    tmpj = 7
                    text_display.color_list_2[tmpi] = (0,255,255)
                    if not card_deck.no_border:
                        text_display.color_list_3[tmpj] = (0,255,255)
                    card_deck.add_border(tmpi,tmpj)
                
                """    
            #print(list(card_deck.border_dictionary))
            #print(sorted(x, key = lambda x: x[0]))
            
            if len(card_deck.flip_dictionary) == 2:
                # note that it is evennt.type not event.key
                if event.type == pygame.K_RETURN :
                    card_deck.check_cards(tmp_1_state_vector_2,tmp_1_state_vector_3,tmp_2_state_vector_2,tmp_2_state_vector_3,transition_to_noise) 
            
            
            if card_deck.check_win():
                first_scene.transition = False
                first_scene.transition_to_end = True
                
            text_display.display_grid(screen)
            pygame.display.flip()

        elif first_scene.transition_to_end and not first_scene.transition:
            first_scene.end_screen()
            #set framerate
            if first_scene.restart:
                card_deck.restart()
                main()

        clock.tick(60)

if __name__ == '__main__':
    main()
