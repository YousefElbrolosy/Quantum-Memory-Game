import pygame
import random
from quantum import Quantum_control
from card import Card
from numpy.random import choice
#possibility of limitin only two cards of the same face to be present (harder) 2 eights instead of 4 eights
# possibility of choosing a different range (with pics)
# possibility of limiting number of grid
# 4 by 4 easy 
# 4 by 8 with four occurences and pics medium 
# 4 by 8 with 2 occurences max and no pics hard and noise?
# need to add special quest cards

class CardDeck():
    cards = []
    cards_xpics_x910 = []
    matrix = [[],[],[],[]]
    matrix_dictionary = {}
    border_dictionary = {}
    flip_dictionary = {}
    checked = False
    no_border = False
    tmpi = 0
    tmpj = 0
    score = 0
    
    def __init__(self):
        pass
    # comment is full deck
    """
    for i in range(1,14):

        cards.append(pygame.transform.scale(pygame.image.load('playing_cards/'+str(i)+'_of_clubs.png'),(64,92.928)))
        cards.append(pygame.transform.scale(pygame.image.load('playing_cards/'+str(i)+'_of_diamonds.png'),(64,92.928)))
        cards.append(pygame.transform.scale(pygame.image.load('playing_cards/'+str(i)+'_of_hearts.png'),(64,92.928)))
        cards.append(pygame.transform.scale(pygame.image.load('playing_cards/'+str(i)+'_of_spades.png'),(64,92.928)))
    cards.append(pygame.transform.scale(pygame.image.load('playing_cards/red_joker.png'),(64,92.928)))
    cards.append(pygame.transform.scale(pygame.image.load('playing_cards/black_joker.png'),(64,92.928)))
    """
    def add_cards(self):
        for i in range(1,9):
            self.cards_xpics_x910.append(Card(pygame.transform.scale(pygame.image.load('playing_cards/'+str(i)+'_of_clubs.png'),(82.6446281,120)),str(i)))     
            self.cards_xpics_x910.append(Card(pygame.transform.scale(pygame.image.load('playing_cards/'+str(i)+'_of_diamonds.png'),(82.6446281,120)),str(i)))
            self.cards_xpics_x910.append(Card(pygame.transform.scale(pygame.image.load('playing_cards/'+str(i)+'_of_hearts.png'),(82.6446281,120)),str(i)))
            self.cards_xpics_x910.append(Card(pygame.transform.scale(pygame.image.load('playing_cards/'+str(i)+'_of_spades.png'),(82.6446281,120)),str(i)))

    def shuffle(self,cards):
        #my method + small modification
        for i in range(len(cards)):
           # cards.insert(random.randint(0,31),cards.pop())
            element = cards.pop(random.randint(0,31))
            cards.append(element)
        

        self.add_to_matrix(cards) 
    def add_to_matrix(self,cards):
        j = 0
        k = 0
        for i in range(len(cards)):
            self.matrix[j].append(cards[i])
            self.matrix_dictionary.update({(j,k):self.matrix[j][k]})
            cards[i].posX += k*82.6446281
            cards[i].posY += j*120
            k+=1
            if i == 7 or i == 15 or i == 23 or i == 31 or i == 39 or i == 47 or i == 55 :
                j+=1
                k = 0
            if j == 4:
                break
            
    def display_dict(self,posX,posY,screen):
        
        for key,val in self.matrix_dictionary.items():
            if val.flipped: 
                screen.blit(val.get_card_img(),(posX+val.posX,posY+val.posY))
            else:
                screen.blit(val.get_back_img(),(posX+val.posX,posY+val.posY))

    def cheat_dict(self,posX,posY,screen):
        for key,val in self.matrix_dictionary.items():
            screen.blit(val.get_card_img(),(posX+val.posX,posY+val.posY))

    
    def add_border(self,i,j):
        if self.matrix_dictionary.get((i,j)) != None:
            self.matrix_dictionary[(i,j)].set_border()
            self.border_dictionary.update({(i,j):self.matrix_dictionary[(i,j)]})
            self.no_border = False
        else: 
            self.no_border = True
    """
    def reset8(self,row_flag, col_flag, superposition_flag_2, superposition_flag_3):
        if len(self.border_dictionary) > 1:
            if (row_flag and not superposition_flag_2) or (col_flag and not superposition_flag_3):
                for key,value in list(self.border_dictionary.items()):
                    value.remove_border()
                    del self.border_dictionary[key]
        
       
    
        if len(self.border_dictionary) == 2:
            if (not superposition_flag_2 or not superposition_flag_3):
                for key,value in list(self.border_dictionary.items()):
                    value.remove_border()
                    del self.border_dictionary[key]
        elif (len(self.border_dictionary) > 2):
            if(col_flag and superposition_flag_2):
                for key,value in list(self.border_dictionary.items()):
                    if len(list(self.border_dictionary.items))>2:
                        value.remove_border()
                        del self.border_dictionary[key] 
    """
    """
    def reset7(self,row_flag, col_flag, superposition_flag_2, superposition_flag_3):
        if len(self.border_dictionary) > 1 and not (superposition_flag_2) and row_flag:
            for key,value in list(self.border_dictionary.items()):
                    value.remove_border()
                    del self.border_dictionary[key]
        if len(self.border_dictionary) > 2 and superposition_flag_2 and row_flag:
            for key,value in list(self.border_dictionary.items()):
                    #if len(self.border_dictionary) > 2:
                    value.remove_border()
                    del self.border_dictionary[key]
        if len(self.border_dictionary) > 1 and not (superposition_flag_3 or superposition_flag_2) and col_flag:
            for key,value in list(self.border_dictionary.items()):
                    value.remove_border()
                    del self.border_dictionary[key]
        if len(self.border_dictionary) > 2 and (superposition_flag_3 or superposition_flag_2) and col_flag:
            for key,value in list(self.border_dictionary.items()):
                    value.remove_border()
                    del self.border_dictionary[key]
    """
    def reset6(self,row_flag, col_flag, superposition_flag_2, superposition_flag_3):
        if(row_flag):
            if len(self.border_dictionary) > 1:
                if not superposition_flag_2:
                    for key,value in list(self.border_dictionary.items()):
                        value.remove_border()
                        del self.border_dictionary[key]
                else:
                    if len(self.border_dictionary) >= 2:
                        for key,value in list(self.border_dictionary.items()):
                            value.remove_border()
                            del self.border_dictionary[key]
        elif(col_flag):
            if len(self.border_dictionary) > 1:
                if not superposition_flag_2:
                    if not superposition_flag_3:
                        for key,value in list(self.border_dictionary.items()):
                            value.remove_border()
                            del self.border_dictionary[key]
                else:
                    if len(self.border_dictionary) >= 2:
                        for key,value in list(self.border_dictionary.items()):
                            value.remove_border()
                            del self.border_dictionary[key]
    def flip(self,i,j,superposition_flag_2,superposition_flag_3, super_prob_2, super_prob_3):
        """
        if len(self.border_dictionary) > 2:
            if superposition_flag_2 or superposition_flag_3:
                if superposition_flag_2 and not superposition_flag_3:
                    measurement_list = choice(list(self.matrix_dictionary), 1, super_prob_2)
        ################## method
        from numpy.random import choice
        
        sampleList = [100, 200, 300, 400, 500]
        randomNumberList = choice(
        sampleList, 5, p=[0.05, 0.1, 0.15, 0.20, 0.5])
        
        print(randomNumberList)
        ##################
        problem is:
        ___________
        this is all the indicies with border
        ------------------------------------

        |
        |

        [(0, 0), (3, 0), (0, 1), (3, 1), (0, 6), (3, 6), (0, 7), (3, 7)] 

        this is the probabilities of column elements in "1" row
        -------------------------------------------------------

        |
        |

        [(0, (0.4999999999999999+0j)), (1, (0.4999999999999999+0j)), (2, 0j), (3, 0j), (4, 0j), (5, 0j), (6, (0.4999999999999999+0j)), (7, (0.4999999999999999+0j))]

        this is probabilities of row elements in 1 column
        -------------------------------------------------

        |
        |

        [(0, (0.7071067811865475+0j)), (1, 0j), (2, 0j), (3, (0.7071067811865475+0j))]


        I need to make something that combines the probabilities of row states and col states into 5 qubit probabilities

        or 

        choose a col_state from the super_prob_3 
        then choose a row_state from the super_prob_2
        
        therefore,

        [(0, 0), (3, 0), (0, 1), (3, 1), (0, 6), (3, 6), (0, 7), (3, 7)]
        probabilities = [[0.5,0.5],[0,25,0,15,0.35,0.25]] --> first list is probabilities of selection of row (they are 2 because there are only 2 in superposition would be 4 if all rows are in super position and consequently in the border dictionary it would be 4 lists coressponding to 8 columns)
                                                          --> second list is probabilities of selection of column
    
        task: is organising border dictionary to be that way
        --> [[(0,0),(0,1),(0,6),(0,7)],
             [(3,0),(3,1),(3,6),(3,7)]]
        """  


        #else:
        self.matrix_dictionary[(i,j)].flip()
        self.flip_dictionary.update({(i,j):self.matrix_dictionary[(i,j)]})
        
        
    def un_flip(self):
        for key,val in list(self.flip_dictionary.items()):
            val.un_flip()
            del self.flip_dictionary[key]
        
        
    def check_cards(self):
        self.checked = True
    
        if list(self.flip_dictionary.values())[0].img_number == list(self.flip_dictionary.values())[1].img_number:
            for (i,j), value in list(self.flip_dictionary.items()):
                #here it is important to display using a matrix because
                #if display depends on card then deleting a matrix element wont affect grid
                
                del self.flip_dictionary[(i,j)]
                #del(self.matrix[i][j])
                del self.matrix_dictionary[(i,j)]
                self.score+=1
        else:
            self.un_flip()

        

        