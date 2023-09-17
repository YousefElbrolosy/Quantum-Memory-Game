import pygame
pygame.init()
class Card():  
    
    def __init__(self,card_img,img_number):
        self.card_img = card_img
        self.img_number = img_number
        self.posX = 0
        self.posY = 0
        self.back_img = pygame.transform.scale(pygame.image.load('data/photos/yellow_back.png'),((82.6446281,120)))
        self.tmp = card_img
        self.border = False
        self.flipped = False
    def get_card_img(self):
        return self.card_img
    def set_card_img(self,img):
        self.card_img = img
    def get_back_img(self):
        return self.back_img
    def set_border(self):
        self.border = True
        
        if self.flipped:
            pygame.draw.rect(self.card_img, (0,255,255), [0, 0,82.6446281 , 120],3, 5)
        else:
            pygame.draw.rect(self.back_img, (0,255,255), [0, 0,82.6446281 , 120],5, 5)
        #old
        #pygame.draw.rect(self.back_img, (0,255,255), [0, 0,82.6446281 , 120], 5)
    def remove_border(self):
        self.border = False
        if self.flipped:
            self.card_img = self.tmp
        else:
            self.back_img = pygame.transform.scale(pygame.image.load('data/photos/yellow_back.png'),((82.6446281,120)))
    def flip(self):
        self.flipped = True
    def un_flip(self):
        self.flipped = False
