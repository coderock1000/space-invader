import math
import random
import pygame

screen_width = 800
screen_height = 500
player_starting_x = 370
player_starting_y = 380
enemy_starting_y_min = 50
enemy_starting_y_max = 150
enemy_speed_x = 4
enemy_speed_y = 40
bullet_speed_y = 10
collision_distance = 27

pygame.init()

screen = pygame.display.set_mode((screen_width,screen_height))

background = pygame.image.load('background.jpg')

pygame.display.set_caption('Space Protector')

pygameImg = pygame.image.load('player.png')
playerx = player_starting_x
playery = player_starting_y
playerx_change = 0

enemyImg = []
enemyx = []
enemyy = []
enemyx_change = []
enemyy_change = []
num_of_enemies = 6
for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('enemy.png'))
    enemyx.append(random.randint(0,screen_width - 64))
    enemyy.append(random.randint(enemy_starting_y_min, enemy_starting_y_max))
    enemyx_change.append(enemy_speed_x)
    enemyy_change.append(enemy_speed_y)

bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = player_starting_y
bulletX_change = 0
bulletY_change = bullet_speed_y
bullet_state = 'ready'

score_value = 0
font = pygame.font.Font('Freesansbold.ttf', 64)
textX = 10
textY = 10


over_font = pygame.font.render('Score : '+ str(score_value),True, (255,255,255))
screen.blit(score, {x,y})

def show_score(x,y):
    