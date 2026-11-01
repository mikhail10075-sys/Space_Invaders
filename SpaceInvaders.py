import math
import random
import pygame

SCREEN_HEIGHT = 900
SCREEN_WIDTH = 900
PLAYER_X = 10
PLAYER_Y = 10
ENEMY_Y_MIN = 850
ENEMY_Y_MAX = 10
BULLET_SPEED = 10
ENEMY_SPEED_X = 4
ENEMY_SPEED_Y = 40
COLLISION_DISTANCE = 30

pygame.init()

screen = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_WIDTH))
background = pygame.image.load('bg.jfif')
pygame.display.set_caption('Space Invaders')

PlayerImg = pygame.image.load('SpaceInvader.png')
PlayerX = PLAYER_X
PlayerY = PLAYER_Y
PlayerX_change = 0

EnemyImg = []
Enemy_X = []
Enemy_Y = []
EnemyX_change = []
EnemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    EnemyImg.append(pygame.image.load('E.png'))
    Enemy_X.append(random.randint(0,SCREEN_WIDTH - 64))
    Enemy_Y.append(random.randint(ENEMY_Y_MAX,ENEMY_Y_MIN))
    EnemyX_change((ENEMY_SPEED_X))
    EnemyY_change.append((ENEMY_SPEED_Y))

BulletImg = pygame.image.load(GUN.png)
BulletStartX = 0
BulletStartY = PLAYER_Y
BulletX_change = 0
BulletY_change= BULLET_SPEED
Bullet_state= 'ready'



pygame.display.update()