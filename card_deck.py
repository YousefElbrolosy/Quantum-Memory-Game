import pygame
import random
from card import Card
#possibility of limitin only two cards of the same face to be present (harder) 2 eights instead of 4 eights
# possibility of choosing a different range
class CardDeck():
    cards = []
    cards_xpics_x910 = []
    matrix = [[],[],[],[]]
    dictionary = {}
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
            self.cards_xpics_x910.append(Card(pygame.transform.scale(pygame.image.load('playing_cards/'+str(i)+'_of_clubs.png'),(82.6446281,120))))     
            self.cards_xpics_x910.append(Card(pygame.transform.scale(pygame.image.load('playing_cards/'+str(i)+'_of_diamonds.png'),(82.6446281,120))))
            self.cards_xpics_x910.append(Card(pygame.transform.scale(pygame.image.load('playing_cards/'+str(i)+'_of_hearts.png'),(82.6446281,120))))
            self.cards_xpics_x910.append(Card(pygame.transform.scale(pygame.image.load('playing_cards/'+str(i)+'_of_spades.png'),(82.6446281,120))))

    def shuffle(self,cards):
        for i in range(len(cards)):
            cards.insert(random.randint(0,31),cards.pop())
        return cards
    def display(self,posX,posY,cards,screen):
        tmp = posX
        j = 0
        #print(len(cards))
        #screen.blit(cards[0].get_card_img(),(posX,posY))
        #screen.blit(pygame.transform.scale(pygame.image.load('playing_cards/'+'2'+'_of_clubs.png'),(82.6446281,120)),(10,10))
        for i in range(len(cards)):
            #displays and adds to a matrix
            screen.blit(cards[i].back_img,(posX,posY))
            
            self.matrix[j].append(cards[i])
            
            posX +=82.6446281
            if i == 7 or i == 15 or i == 23 or i == 31 or i == 39 or i == 47 or i == 55 :
                posX = tmp
                posY+=120
                j+=1
    
    def add_border(self,i,j):
        self.matrix[i][j].set_border()
        self.dictionary.update({(i,j):self.matrix[i][j]})

    def reset8(self):
        for key,value in self.dictionary.items():
            value.remove_border()

    """
    def set_border(self,i,j):
        self.matrix[i][j].set_border(True)
        self.temp[(i,j)] = self.matrix[i].pop(j)
    
    def display_border(self,index1,index2):
        self.border_matrix[index1][index2] = True
        (self.matrix[index1][index2]).set_border(self.border_matrix[index1][index2])
    
    def reset(self,cards):
        for i in range(len(cards)):
            cards[i].update_img()
    def reset2(self):
        self.border_matrix = [[False,False,False,False,False,False,False,False],
              [False,False,False,False,False,False,False,False],
              [False,False,False,False,False,False,False,False],
              [False,False,False,False,False,False,False,False]]
    def reset3(self,stack):
        # here I want to re insert any removed element back into its position
        # I think that I will need to make a hashmap
        if len(hmap) > 0:
            matrix[hmap.get_val()]
    """
