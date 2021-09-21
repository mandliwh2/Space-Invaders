import pygame
import random
import math

# initialize the pygame module
pygame.init()
# creating the screen
screen = pygame.display.set_mode((800, 600))  # the size of the screen
pygame.display.set_caption("Space Invaders")  # the title of the window
icon = pygame.image.load("spaceship.png")  # loading the icon
pygame.display.set_icon(icon)  # applying the icon to the window

# background

backgroundImg = pygame.image.load("background.png")

# player
playerImg = pygame.image.load("player.png")
playerX = 368
playerY = 500
playerX_change = 1


def player(x, y):
    screen.blit(playerImg, (x, y))


# enemy

enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
enemy_number = 6
for i in range(enemy_number):
    enemyImg.append(pygame.image.load("enemy.png"))
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(0, 100))
    enemyX_change.append(5)
    enemyY_change.append(20)


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


# bullet

bulletImg = pygame.image.load("bullet.png")
bulletX = 0
bulletY = 480
bulletY_change = 5
bulletX_change = 0
bullet_state = "ready"


def bullet_fire(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 12, y + 10))


# score

score_value = 0
font = pygame.font.Font("freesansbold.ttf", 32)
scoreX = 0
scoreY = 0

gameOverX = 200
gameOverY = 250
fontS = pygame.font.Font("freesansbold.ttf", 64)

fontZ = pygame.font.Font("freesansbold.ttf", 32)
igX = 550
igY = 550


def show_ig(x, y):
    ig = fontZ.render("@MANDLIWH2", True, (255, 255, 255))
    screen.blit(ig, (igX, igY))


def gameOver(x, y):
    game_over = fontS.render("GAME OVER", True, (255, 255, 255))
    screen.blit(game_over, (gameOverX, gameOverY))


def show_score(x, y):
    score = font.render("SCORE : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False


# main game loop
running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(backgroundImg, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                playerX_change += 8
            if event.key == pygame.K_LEFT:
                playerX_change -= 8
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bulletX = playerX
                    bullet_fire(bulletX, bulletY)

    playerX += playerX_change
    enemyX += enemyX_change
    if playerX >= 736:
        playerX = 736
    if playerX <= 0:
        playerX = 0

    for i in range(enemy_number):
        if enemyY[i] > 440:
            for J in range(enemy_number):
                enemyY[J] = 2000
            gameOver(gameOverX, gameOverY)
            show_ig(igX, igY)
            break

        enemyX[i] += enemyX_change[i]
        if enemyX[i] >= 736:
            enemyX_change[i] = -5
            enemyY[i] += 20
        if enemyX[i] <= 0:
            enemyX_change[i] = 4
            enemyY[i] += 20
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = 400 - 32
            enemyY[i] = random.randint(50, 150)
        enemy(enemyX[i], enemyY[i], i)

    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state == "fire":
        bullet_fire(bulletX, bulletY)
        bulletY -= bulletY_change
    show_score(scoreX, scoreY)
    player(playerX, playerY)

    pygame.display.update()
