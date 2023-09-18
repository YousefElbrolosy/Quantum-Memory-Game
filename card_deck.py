import pygame
import random
from card import Card
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
        for i in range(len(cards)):
            cards.insert(random.randint(0,31),cards.pop())
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

    def reset8(self):
        if len(self.border_dictionary) > 1:
            for key,value in self.border_dictionary.items():
                value.remove_border()
                
    def flip(self,i,j):
        self.matrix_dictionary[(i,j)].flip()
        self.flip_dictionary.update({(i,j):self.matrix_dictionary[(i,j)]})

    def un_flip(self):
        for key,val in list(self.flip_dictionary.items()):
            val.un_flip()
            del self.flip_dictionary[key]

    def check_cards(self):
        self.checked = True
        print(list(self.flip_dictionary.values())[0].img_number)
        print(list(self.flip_dictionary.values())[1].img_number)
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