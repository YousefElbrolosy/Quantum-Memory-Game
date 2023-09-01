import pygame
pygame.init()
class Card():
    back_img = pygame.transform.scale(pygame.image.load('data/photos/yellow_back.png'),((82.6446281,120)))
    def __init__(self,card_img):
        self.card_img = card_img
    def get_card_img(self):
        return self.card_img