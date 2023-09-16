import pygame
import random
import time
from card import Card
#possibility of limitin only two cards of the same face to be present (harder) 2 eights instead of 4 eights
# possibility of choosing a different range
class CardDeck():
    cards = []
    cards_xpics_x910 = []
    matrix = [[],[],[],[]]
    border_dictionary = {}
    flip_dictionary = {}
    flipped_list = []
    checked = False
    tmpi = 0
    tmpj = 0
    
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
        return cards
    def add_to_matrix(self,cards):
        j = 0
        k = 0
        for i in range(len(cards)):
            self.matrix[j].append(cards[i])
            cards[i].posX += k*82.6446281
            cards[i].posY += j*120
            k+=1
            if i == 7 or i == 15 or i == 23 or i == 31 or i == 39 or i == 47 or i == 55 :
                j+=1
                k = 0
            if j == 4:
                break
            
                

    def display_matrix(self,posX,posY,screen):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if self.matrix[i][j].flipped:
                    screen.blit(self.matrix[i][j].get_card_img(),(posX+self.matrix[i][j].posX,posY+self.matrix[i][j].posY))
                else:
                    screen.blit(self.matrix[i][j].get_back_img(),(posX+self.matrix[i][j].posX,posY+self.matrix[i][j].posY))
                
                    

    def display(self,posX,posY,cards,screen):
        tmp = posX
        j = 0
        #print(len(cards))
        #screen.blit(cards[0].get_card_img(),(posX,posY))
        #screen.blit(pygame.transform.scale(pygame.image.load('playing_cards/'+'2'+'_of_clubs.png'),(82.6446281,120)),(10,10))
        for i in range(len(cards)):
            #displays and adds to a matrix
            if cards[i].flipped:
                screen.blit(cards[i].get_card_img(),(posX,posY))
            else:
                screen.blit(cards[i].get_back_img(),(posX,posY))
            self.matrix[j].append(cards[i])
            
            posX +=82.6446281
            if i == 7 or i == 15 or i == 23 or i == 31 or i == 39 or i == 47 or i == 55 :
                posX = tmp
                posY+=120
                j+=1
    def cheat(self,posX,posY,screen):
        tmp = posX
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                screen.blit(self.matrix[i][j].get_card_img(),(posX,posY))
                posX +=82.6446281
                if j == 7: 
                    posX = tmp
                    posY+=120
                    break
    
    def add_border(self,i,j):
        self.matrix[i][j].set_border()
        self.border_dictionary.update({(i,j):self.matrix[i][j]})

    def reset8(self):
        if len(self.border_dictionary) > 1:
            for key,value in self.border_dictionary.items():
                value.remove_border()
                
    def flip(self,i,j):
        self.matrix[i][j].flip()
        self.flip_dictionary.update({(i,j):self.matrix[i][j]})
        self.flipped_list.append(self.matrix[i][j])

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
                del(self.matrix[i][j])
                print(len(self.matrix))
                print(len(self.matrix[0]))
        else:
            self.un_flip()