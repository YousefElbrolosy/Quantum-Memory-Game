import pygame
pygame.init()
screen = pygame.display.set_mode((1366,725))
import random
cards = []
for i in range(1,14):
    cards.append(pygame.image.load('playing_cards/'+str(i)+'_of_clubs.png'))
    cards.append(pygame.image.load('playing_cards/'+str(i)+'_of_diamonds.png'))
    cards.append(pygame.image.load('playing_cards/'+str(i)+'_of_hearts.png'))
    cards.append(pygame.image.load('playing_cards/'+str(i)+'_of_spades.png'))
cards.append(pygame.image.load('playing_cards/red_joker.png'))
cards.append(pygame.image.load('playing_cards/black_joker.png'))

def shuffle(cards):
    shuffled = cards
    for i in range(len(cards)):
        cards.insert(random.randint(0,51),cards.pop())
    return shuffled
def display(posX,posY,cards):
    tmp = posX
    for i in range(len(cards)):
        pygame.transform.scale(cards[i],(64,93))
        screen.blit(cards[i],(posX,posY))
        posX +=5
        if i == 7 or i == 15 or i == 23 or i == 31 or i == 39 or i == 47 or i == 55 :
            posX = tmp
            posY+=10
    print("drawn successfully")

