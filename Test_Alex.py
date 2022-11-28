import pygame
from engi1020.arduino.api import *
from time import sleep
import random
from math import *
import os
pygame.init()
dis = pygame.display.set_mode((800, 600))
pygame.display.update()
pygame.display.set_caption("Dodge")
game_over = False
fps = pygame.time.Clock()

# colours
blue = (0, 0, 255)
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
yellow = (255,255,0)

# display
displaysize = [800,600]
dis = pygame.display.set_mode((displaysize[0], displaysize[1]))
startup_screen = True
backround = pygame.image.load(os.path.join('venv', 'gamebg.png'))
# Player Values
p1size = 25
p1speed = 4
p1pos = [displaysize[0]/2,displaysize[1]/2]
p1bullets = []
p1bulletcooldown = 0
p1lives = 3
p1score = 0
p1image = pygame.image.load(os.path.join('venv', 'p1Sprite.png'))
p1sprite = pygame.transform.scale(p1image, p1size)



p2size = 25
p2speed = 4
p2pos = [0, displaysize[1]/3]
p2bullets = []
p2bulletcooldown = 0
p2lives = 3
p2score = 0
p2image = pygame.image.load(os.path.join('venv', 'p2image.gif'))
p2sprite = pygame.transform.scale(p2image, p2size)

# Bullet Values
bulletsize = 5
bulletspeed = 10

# Displaying Text
font = pygame.font.Font('freesansbold.ttf', 32)
def message (msg,colour,x,y):
    mesg = font.render(msg, True, colour)
    dis.blit(mesg, [x, y])
def move_player(speed, position, joystick,player, size):
    position[0] += joystick[0] * speed
    player = pygame.draw.circle(dis, red, position, size)
    for o in oblist:
        if pygame.Rect.colliderect(player,o):
            position[0] -= joystick[0] * speed
    position[1] += joystick[1] * speed
    player = pygame.draw.rect(dis, red, [position[0], position[1], size[0], size[1]])
    for o in oblist:
        if pygame.Rect.colliderect(player,o):
            position[1] -= joystick[1] * speed

    if position[0] > displaysize[0] - size:
        position[0] = displaysize[0] - size
    if position[0] < 0:
        position[0] = 0
    if position[1] > displaysize[1] - p1size[1]:
        position[1] = displaysize[1] - p1size[1]
    if position[1] < 0:
        position[1] = 0
    return position

def move_bullet(speed, position, angle):
    position[0] += speed * cos(angle)
    position [1] += speed * sin(angle)
    return position



while not game_over:
    #Updates timers
    if p1bulletcooldown > 0:
        p1bulletcooldown -= 1/60
    else:
        p1bulletcooldown = 0

    if p2bulletcooldown > 0:
        p2bulletcooldown -= 1/60
    else:
        p2bulletcooldown = 0

    # Closes Window if X is pressed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    keys = pygame.key.get_pressed()

#Joystick Movement
    joystick = [0, 0]
    if keys[pygame.K_w]:
        joystick[1] = -1
    elif keys[pygame.K_s]:
        joystick[1] = 1
    if keys[pygame.K_a]:
        joystick[0] = -1
    elif keys[pygame.K_d]:
        joystick[0] = 1
    #joystick.append(joystick_get_x())
    #joystick.append(joystick_get_y())

    keycontrols = [0, 0]
    if keys[pygame.K_UP]:
        keycontrols[1] = -1
    elif keys[pygame.K_DOWN]:
        keycontrols[1] = 1
    if keys[pygame.K_LEFT]:
        keycontrols[0] = -1
    elif keys[pygame.K_RIGHT]:
        keycontrols[0] = 1

     # Visual output
    dis.fill(black)
    dis.blit(backround, (0,0))
    o1 = pygame.draw.rect(dis, yellow, [displaysize[0] / 3, displaysize[1] / 3, 35, 35])
    o2 = pygame.draw.rect(dis, yellow, [displaysize[0] * 2 / 3, displaysize[1] / 3, 30, 30])
    o3 = pygame.draw.rect(dis, yellow, [displaysize[0] / 3, displaysize[1] * 2 / 3, 25, 25])
    o4 = pygame.draw.rect(dis, yellow, [displaysize[0] * 2 / 3, displaysize[1] * 2 / 3, 40, 40])
    o5 = pygame.draw.rect(dis, yellow, [displaysize[0] * 1 / 6, displaysize[1] * 1 / 6, 35, 35])
    o6 = pygame.draw.rect(dis, yellow, [displaysize[0] * 5 / 6, displaysize[1] * 5 / 6, 30, 30])
    o7 = pygame.draw.rect(dis, yellow, [displaysize[0] * 1 / 6, displaysize[1] * 5 / 6, 25, 25])
    o8 = pygame.draw.rect(dis, yellow, [displaysize[0] * 5 / 6, displaysize[1] * 1 / 6, 20, 20])
    o9 = pygame.draw.rect(dis, yellow, [displaysize[0] * 1 / 6, displaysize[1] * 1 / 2, 20, 20])
    o10 = pygame.draw.rect(dis, yellow, [displaysize[0] * 1 / 2, displaysize[1] * 1 / 6, 40, 40])
    o11 = pygame.draw.rect(dis, yellow, [displaysize[0] * 1 / 2, displaysize[1] * 5 / 6, 30, 30])
    o12 = pygame.draw.rect(dis, yellow, [displaysize[0] * 5 / 6, displaysize[1] * 1 / 2, 25, 25])
    o13 = pygame.draw.rect(dis, yellow, [displaysize[0] * 1 / 2, displaysize[1] * 6 / 10, 35, 35])
    oblist = [o1, o2, o3, o4, o5, o6, o7, o8, o9, o10, o11, o12, o13]

    p1 = pygame.draw.rect(dis, black, [p1pos[0], p1pos[1], p1size[0], p1size[1]], 1)
    p2 = pygame.draw.rect(dis, black, [p2pos[0], p2pos[1], p2size[0], p2size[1]])

    dis.blit(p1sprite, (p1.x,p1.y))
    dis.blit(p2sprite, (p2.x, p2.y))


    for bullet in p1bullets:
        new_pos = move_bullet(bulletspeed, bullet[0], bullet[1])
        b = pygame.draw.circle(dis, white, new_pos, bulletsize)
        if pygame.Rect.colliderect(b,p2):
            p2lives -= 1
            p1bullets.remove(bullet)
        else:
            for obstacle in oblist:
                if pygame.Rect.colliderect(b,obstacle):
                    p1bullets.remove(bullet)
    for bullet in p2bullets:
        new_pos = move_bullet(bulletspeed, bullet[0], bullet[1])
        b = pygame.draw.circle(dis, white, new_pos, bulletsize)
        if pygame.Rect.colliderect(b,p1):
            p1lives -= 1
            p2bullets.remove(bullet)
        for obstacle in oblist:
            if pygame.Rect.colliderect(b,obstacle):
                p2bullets.remove(bullet)
    message("P1 Score: " + str(p1score), white, 0, 0)
    message("P2 Score: " + str(p2score), white, displaysize[0] / 1.3, 0)
    pygame.display.update()

    #Win conditions
    if p1lives == 0:
        sleep(1)
        p2score += 1
        p1lives = 3
    elif p2lives == 0:
        sleep(1)
        p1score += 1
        p2lives = 3

    if p1score == 5:
        dis.fill(black)
        message("Player One Wins", red, displaysize[0]/3, displaysize[1]/2)
        pygame.display.update()
        sleep(3)
        game_over = True
    if p2score == 5:
        dis.fill(black)
        message("Player Two Wins", blue, displaysize[0]/3, displaysize[1]/2)
        pygame.display.update()
        sleep(3)
        game_over = True

        # Move entities
    p1pos = move_player(p1speed, p1pos, joystick, p1, p1size)
    p2pos = move_player(p2speed, p2pos, keycontrols, p2,p2size)
    if keys[pygame.K_SPACE] and p1bulletcooldown == 0:
        bulletposition = [p1pos[0] + p1size[0] / 2, p1pos[1] + p1size[1] / 2]
        p1bullets.append([bulletposition, 0.8])
        p1bulletcooldown = 0.25

    if keys[pygame.K_RSHIFT] and p2bulletcooldown == 0:
        bulletposition = [p2pos[0] + p2size[0] / 2, p2pos[1] + p2size[1] / 2]
        p2bullets.append([bulletposition, 0.8])
        p2bulletcooldown = 0.25

    fps.tick(60)
pygame.quit()
quit()