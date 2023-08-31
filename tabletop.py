import pygame
pygame.init()
screen = pygame.display.set_mode((1366,725))
import random
cards = []
cards_xpics_x910 = []
matrix = [[],[],[],[]]
for i in range(1,14):

    cards.append(pygame.transform.scale(pygame.image.load('playing_cards/'+str(i)+'_of_clubs.png'),(64,92.928)))
    cards.append(pygame.transform.scale(pygame.image.load('playing_cards/'+str(i)+'_of_diamonds.png'),(64,92.928)))
    cards.append(pygame.transform.scale(pygame.image.load('playing_cards/'+str(i)+'_of_hearts.png'),(64,92.928)))
    cards.append(pygame.transform.scale(pygame.image.load('playing_cards/'+str(i)+'_of_spades.png'),(64,92.928)))
cards.append(pygame.transform.scale(pygame.image.load('playing_cards/red_joker.png'),(64,92.928)))
cards.append(pygame.transform.scale(pygame.image.load('playing_cards/black_joker.png'),(64,92.928)))


for i in range(1,9):

    cards_xpics_x910.append(pygame.transform.scale(pygame.image.load('playing_cards/'+str(i)+'_of_clubs.png'),(82.6446281,120)))
    cards_xpics_x910.append(pygame.transform.scale(pygame.image.load('playing_cards/'+str(i)+'_of_diamonds.png'),(82.6446281,120)))
    cards_xpics_x910.append(pygame.transform.scale(pygame.image.load('playing_cards/'+str(i)+'_of_hearts.png'),(82.6446281,120)))
    cards_xpics_x910.append(pygame.transform.scale(pygame.image.load('playing_cards/'+str(i)+'_of_spades.png'),(82.6446281,120)))



def shuffle(cards):
    shuffled = cards
    for i in range(len(cards)):
        cards.insert(random.randint(0,31),cards.pop())
    return shuffled
def display(posX,posY,cards):
    tmp = posX
    j = 0
    for i in range(len(cards)):
        screen.blit(cards[i],(posX,posY))
        matrix[j].append(cards[i])
        posX +=82.6446281
        if i == 7 or i == 15 or i == 23 or i == 31 or i == 39 or i == 47 or i == 55 :
            posX = tmp
            posY+=120
            j+=1

