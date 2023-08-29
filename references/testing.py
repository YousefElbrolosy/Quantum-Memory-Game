import pygame
import random
#for anything with sound
from pygame import mixer
#initialise
pygame.init()
# creating the screen
screen = pygame.display.set_mode((800,600))
#background image
bgImg = pygame.image.load('space.jpg')
#background sounds
mixer.music.load('space.wav')
#-1 means on loop
mixer.music.play(-1)
#Title and Icon
pygame.display.set_caption("Quantum Memory")
icon = pygame.image.load('qubit.png')
pygame.display.set_icon(icon)

#player
playerImg = pygame.image.load('spaceship.png')
playerX = 370
playerY = 480
playerX_change =0
def player(x,y):
    #blit means to draw
    screen.blit(playerImg,(x,y))

#enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
no_enemies = 6



for i in range(no_enemies):

    enemyImg.append(pygame.image.load('alien.png'))
    enemyX.append(random.randint(0,736))
    enemyY.append(random.randint(50,150))
    enemyX_change.append(0.6)
    enemyY_change.append(40)

def respawn(i):
    global enemyX
    global enemyY
    enemyX[i] = random.randint(0,735)
    enemyY[i] = random.randint(50,150)


def enemy(x,y,i):
    #blit means to draw
    screen.blit(enemyImg[i],(x,y))

#Bullet
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 1.5
bullet_state = "ready"

def fire_bullet(x,y):
    global bullet_state 
    bullet_state = "fire"
    screen.blit(bulletImg,(x+16,y+10))

#Score
score = 0
font = pygame.font.Font('freesansbold.ttf',32)

textX = 10
textY = 10

def show_score(x,y):
   score_value =font.render("Score is: " + str(score),True,(255,255,255))
   screen.blit(score_value, (x,y))

#Game over
over_font = pygame.font.Font('freesansbold.ttf',64)
def game_over_text():
   over_text =over_font.render("GAME OVER",True,(255,255,255))
   screen.blit(over_text, (200,250))
#game loop
running = True
flag = False
while running:
    #RGB
    screen.fill((0,255,0))
    #Bg
    screen.blit(bgImg,(0,0))

    enemy_rect = []
    for i in range(no_enemies):
        enemy_rect.append(pygame.Rect((enemyX[i],enemyY[i]),(32,32)))

    bullet_rect = pygame.Rect((bulletX,bulletY),(16,16))
    ship_rect = pygame.Rect((playerX,playerY),(64,64))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.5
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.5
            if event.key == pygame.K_SPACE and bullet_state == "ready":
                # mixer.sound because it is a short sound
                bullet_sound = mixer.Sound('lazer.wav')
                # no -1 because w dont want loop
                bullet_sound.play()
                bulletX = playerX
                fire_bullet(bulletX,bulletY)  
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    
    #boundaries
    playerX += playerX_change
    if playerX <=0 :
        playerX = 0
    elif playerX >=736:
        playerX = 736


    for i in range(no_enemies):
        enemyX[i] += enemyX_change[i]
        if enemyX[i] <=0 or enemyX[i] >=736:
            enemyX_change[i] = -enemyX_change[i]
            enemyY[i] += enemyY_change[i]
        #collision
        if enemy_rect[i].colliderect(bullet_rect):
            # mixer.sound because it is a short sound
            collision_sound = mixer.Sound('collision.wav')
            # no -1 because w dont want loop
            #check how to control volume
            collision_sound.set_volume(5.0)
            collision_sound.play()
            score+=1
            bulletY = 480
            bullet_state = "ready"
            respawn(i)
        if enemy_rect[i].colliderect(ship_rect):
            explosion_sound = mixer.Sound('explosion.mp3')
            explosion_sound.play()
            
            for j in range(no_enemies):
                enemyY[j] = 2000
            flag = True
            
            break

        enemy(enemyX[i],enemyY[i],i)
    #bullet movement

    if bulletY<0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state == "fire":
        fire_bullet(bulletX,bulletY)  
        bulletY -= bulletY_change

    
    

    player(playerX,playerY)
    if flag == True:
        screen.blit(pygame.font.Font('freesansbold.ttf',64).render("GAME OVER",True,(255,255,255)), (200,250))
    show_score(textX,textY)
    pygame.display.update()