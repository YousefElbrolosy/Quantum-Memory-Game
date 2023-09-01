import pygame
pygame.init()
class Card():
    #back_img = pygame.transform.scale(pygame.image.load('data/photos/card_back.jpg'),((64,92.928)))
    def __init__(self,card_img):
        self.card_img = card_img
    def get_card_img(self):
        return self.card_img