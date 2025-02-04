import random

import pygame
pygame.init()
screen_width=800
screen_height=600

gameWindow = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Space Game")
# icon = pygame.image.load
closewindow  =False
white= (255,255,255)

#player
playerImage = pygame.image.load('alien.png')
playerX = 370
playerY = 480
block_update=0.3
playerX_change=0
#player
def player(x,y):
    gameWindow.blit(playerImage,(x,y))

#enemy
enemyImage = pygame.image.load('meteor.png')
# enemyX = 370
# enemyY = 50
enemyX = random.randint(0, 736)
enemyY = random.randint(50,150)
enemyX_change=4
enemyY_change=40
def enemy(x,y):
    gameWindow.blit(enemyImage,(x,y))

# bullet makeing
bulletImage = pygame.image.load('ammo.png')
bulletX=0
bulletY=480
bullet_change=10
bullet_state="ready"

def fireBullet(x ,y):
    global bullet_state
    gameWindow.blit(bulletImage,(x+16, y+12))


while not closewindow:
    gameWindow.fill(white)
    for event in  pygame.event.get():
        if event.type==pygame.QUIT:
            closewindow=True

        if event.type== pygame.KEYDOWN:
            if event.key ==pygame.K_LEFT:
                playerX_change = -block_update
            if event.key ==pygame.K_RIGHT:
                playerX_change = block_update
        if event.type== pygame.KEYUP:
            if event.key ==pygame.K_LEFT:
                playerX_change = 0
            if event.key ==pygame.K_RIGHT:
                playerX_change = 0
            if event.key ==pygame.K_SPACE:
                bulletX=playerX
                fireBullet(bulletX,bulletY)
    playerX+= playerX_change

    if playerX <=0:
        playerX=0
    elif playerX>=736:
        playerX =736
    #enemy movement
    enemyX+=enemyX_change
    if enemyX <=0:
        enemyX_change=0.4
        enemyY+= enemyY_change
    elif enemyX>=736:
        enemyX_change = -0.4
        enemyY+= enemyY_change

    player(playerX,playerY)
    enemy(enemyX,enemyY)
    pygame.display.update()
