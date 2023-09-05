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
    tmpi = 0
    tmpj = 0
    border_matrix = [[False,False,False,False,False,False,False,False],
              [False,False,False,False,False,False,False,False],
              [False,False,False,False,False,False,False,False],
              [False,False,False,False,False,False,False,False]]
    
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
            self.cards_xpics_x910.append(Card(pygame.transform.scale(pygame.image.load('playing_cards/'+str(i)+'_of_clubs.png'),(82.6446281,120)),str(i)+'_of_clubs.png'))     
            self.cards_xpics_x910.append(Card(pygame.transform.scale(pygame.image.load('playing_cards/'+str(i)+'_of_diamonds.png'),(82.6446281,120)),str(i)+'_of_diamonds.png'))
            self.cards_xpics_x910.append(Card(pygame.transform.scale(pygame.image.load('playing_cards/'+str(i)+'_of_hearts.png'),(82.6446281,120)),str(i)+'_of_hearts.png'))
            self.cards_xpics_x910.append(Card(pygame.transform.scale(pygame.image.load('playing_cards/'+str(i)+'_of_spades.png'),(82.6446281,120)),str(i)+'_of_spades.png'))

    def shuffle(self,cards):
        for i in range(len(cards)):
            cards.insert(random.randint(0,31),cards.pop())
        self.add_to_matrix(cards)   
        return cards
    def add_to_matrix(self,cards):
        j = 0
        for i in range(len(cards)):
            self.matrix[j].append(cards[i])
            if i == 7 or i == 15 or i == 23 or i == 31 or i == 39 or i == 47 or i == 55 :
                j+=1
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
    def cheat(self,posX,posY,cards,screen):
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
                screen.blit(cards[i].get_card_img(),(posX,posY))
            self.matrix[j].append(cards[i])
            
            posX +=82.6446281
            if i == 7 or i == 15 or i == 23 or i == 31 or i == 39 or i == 47 or i == 55 :
                posX = tmp
                posY+=120
                j+=1
    
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
        for value in self.flipped_list:
            value.un_flip()
            self.flipped_list.remove(value)

    def check_cards(self):
        if list(self.flip_dictionary.values())[0].img_text == list(self.flip_dictionary.values())[1].img_text:
            for (i,j), value in self.flip_dictionary.items():
                del self.matrix[i][j]
                del value
        else:
            self.un_flip()