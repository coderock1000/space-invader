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
    enemyx.append(random.randint(0, screen_width - 64))
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
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10

def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def game_over_text():
    over_font = font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_font, (200, 250))

def player(x, y):
    screen.blit(pygameImg, (x, y))

def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = 'fire'
    screen.blit(bulletImg, (x + 16, y + 10))

def iscollision(enemyx, enemyy, bulletX, bulletY):
    distance = math.sqrt((enemyx - bulletX) ** 2 + (enemyy - bulletY) ** 2)
    return distance < collision_distance

running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerx_change = -5
            if event.key == pygame.K_RIGHT:
                playerx_change = 5
            if event.key == pygame.K_SPACE and bullet_state == 'ready':
                bulletX = playerx
                fire_bullet(bulletX, bulletY)
        if event.type == pygame.KEYUP:
            if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                playerx_change = 0

    playerx += playerx_change
    playerx = max(0, min(playerx, screen_width - 64))

    for i in range(num_of_enemies):
        if enemyy[i] > 340:
            for j in range(num_of_enemies):
                enemyy[j] = 2000
            game_over_text()
            running = False
            break

        enemyx[i] += enemyx_change[i]
        if enemyx[i] <= 0 or enemyx[i] >= screen_width - 64:
            enemyx_change[i] *= -1
            enemyy[i] += enemyy_change[i]

        if iscollision(enemyx[i], enemyy[i], bulletX, bulletY):
            bulletY = player_starting_y
            bullet_state = 'ready'
            score_value += 1
            enemyx[i] = random.randint(0, screen_width - 64)
            enemyy[i] = random.randint(enemy_starting_y_min, enemy_starting_y_max)

        enemy(enemyx[i], enemyy[i], i)

    if bulletY <= 0:
        bulletY = player_starting_y
        bullet_state = 'ready'
    elif bullet_state == 'fire':
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    player(playerx, playery)
    show_score(textX, textY)
    pygame.display.update()  