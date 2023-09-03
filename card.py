import pygame
pygame.init()
class Card():  
    def __init__(self,card_img):
        self.card_img = card_img
        self.back_img = pygame.transform.scale(pygame.image.load('data/photos/yellow_back.png'),((82.6446281,120)))
        self.border = False
    def get_card_img(self):
        return self.card_img
    def set_border(self):
        self.border = True
        pygame.draw.rect(self.back_img, (0,255,255), [0, 0,82.6446281 , 120], 5)
    def remove_border(self):
        self.border = False
        self.back_img = pygame.transform.scale(pygame.image.load('data/photos/yellow_back.png'),((82.6446281,120)))