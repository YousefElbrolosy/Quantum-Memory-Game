import pygame
import random
import sympy as sp
from sympy import Eq, solve_linear_system, Matrix
from quantum import Quantum_control
from card import Card
import operator
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
    deleted_dictionary = {}
    border_dictionary = {}
    flipped = False
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

    
    def add_border(self,i,j,color):
        if self.matrix_dictionary.get((i,j)) != None:
            self.matrix_dictionary[(i,j)].set_border(color)
            self.border_dictionary.update({(i,j):self.matrix_dictionary[(i,j)]})
            self.no_border = False
        else: 
            self.border_dictionary.update({(i,j):self.deleted_dictionary[(i,j)]})
            self.no_border = True    
        
            #self.supposed_border_dictionary.update({(i,j):self.matrix_dictionary[(i,j)]})
            
        
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
                if not superposition_flag_3:
                    for key,value in list(self.border_dictionary.items()):
                        value.remove_border()
                        del self.border_dictionary[key]
                        
                else:
                    if len(self.border_dictionary) >= 2:
                        for key,value in list(self.border_dictionary.items()):
                            value.remove_border()
                            del self.border_dictionary[key]
                        
    def flip(self, super_prob_2, super_prob_3, noise):
        dice = random.randint(0,3)
        if not noise or dice == 0 or dice == 1:
            matrix = self.border_dictionary_2D()
            row_measurement = random.choices(matrix,weights= super_prob_2, k = 1)
            col_measurement = random.choices(list(row_measurement[0].keys()), weights = super_prob_3, k = 1)
            flip_key = col_measurement[0]
            
            if(self.matrix_dictionary.get(flip_key) != None):
                self.matrix_dictionary[flip_key].flip()
                self.flip_dictionary.update({flip_key:self.matrix_dictionary[flip_key]})
                self.flipped = True
            else:
                self.flipped = False
        elif noise or dice == 2:
            flip_key = (random.randint(0,3),random.randint(0,8))
            if(self.matrix_dictionary.get(flip_key) != None):
                self.matrix_dictionary[flip_key].flip()
                self.flip_dictionary.update({flip_key:self.matrix_dictionary[flip_key]})
                self.flipped = True
            else:
                self.flipped = False
            
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
        #note the order of both prob and elements in border dict

        #else:
        #self.matrix_dictionary[(i,j)].flip()
        #self.flip_dictionary.update({(i,j):self.matrix_dictionary[(i,j)]})
        
        
    def un_flip(self):
        for key,val in list(self.flip_dictionary.items()):
            val.un_flip()
            del self.flip_dictionary[key]
            
    def check_cards(self,state_vector_2,state_vector_3):
        self.checked = True
        print(state_vector_2)
        print(state_vector_3)
        if list(self.flip_dictionary.values())[0].img_number == list(self.flip_dictionary.values())[1].img_number:
            if self.entanglement_witness(state_vector_2,state_vector_3):
                self.score += 5
            self.score+=1
            for (i,j), value in list(self.flip_dictionary.items()):
                #here it is important to display using a matrix because
                #if display depends on card then deleting a matrix element wont affect grid
                
                del self.flip_dictionary[(i,j)]
                #del(self.matrix[i][j])
                self.deleted_dictionary.update({(i,j):self.matrix_dictionary[(i,j)]})
                del self.matrix_dictionary[(i,j)]
                
            
                
                #self.score+=5
                
        else:
            self.un_flip()
    
    def border_dictionary_2D(self):
        
        z = sorted(self.border_dictionary, key= operator.itemgetter(0))

        tmp = z[0][0]
        #print(tmp)
        matrix = [{}]
        k = 0
        for (i,j) in z:
            if i == tmp:
                matrix[k].update({(i,j):self.border_dictionary[(i,j)]})
            else:
                matrix.append({})
                k+=1
                matrix[k].update({(i,j):self.border_dictionary[(i,j)]})
                tmp = i
        return matrix
        

    #def oscillate(self,prob_list_2,prob_list_3):
        matrix = self.border_dictionary_2D()
        """
        --> [[(0,0),(0,1),(0,6),(0,7)],
             [(3,0),(3,1),(3,6),(3,7)]]

             [
              [(0,0),(3,0)],
              [(0,1),(3,1)],
              [(0,6),(3,6)],
              [(0,7),(3,7)]
              ]
            each row 
        """

    def entanglement_witness(self,state_vector_2,state_vector_3):
        
        x0,x1,y0,y1 = sp.symbols('x0 x1 y0 y1')
        eq1 = Eq(x0*y0, state_vector_2[0])
        eq2 = Eq(x0*y1, state_vector_2[1])
        eq3 = Eq(x1*y0, state_vector_2[2])
        eq4 = Eq(x1*y1, state_vector_2[3])

        result_2 = sp.solve([eq1,eq2,eq3,eq4],(x0,x1,y0,y1))

        x0,x1,y0,y1,z0,z1 = sp.symbols('x0 x1 y0 y1 z0 z1')
        eq1 = Eq(x0*y0*z0, state_vector_3[0])
        eq2 = Eq(x0*y0*z1, state_vector_3[1])
        eq3 = Eq(x0*y1*z0, state_vector_3[2])
        eq4 = Eq(x0*y1*z1, state_vector_3[3])
        eq5 = Eq(x1*y0*z0, state_vector_3[4])
        eq6 = Eq(x1*y0*z1, state_vector_3[5])
        eq7 = Eq(x1*y1*z0, state_vector_3[6])
        eq8 = Eq(x1*y1*z1, state_vector_3[7])

        result_3 = sp.solve([eq1,eq2,eq3,eq4,eq5,eq6,eq7,eq8],(x0,x1,y0,y1,z0,z1))

        if len(result_2) == 0 or len(result_3) == 0:
            return True
        else:
            return False
