import pygame
from engi1020.arduino.api import *
from time import sleep
import random
from math import *

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

# Player Values
p1size = [30,50]
p1speed = 4
p1pos = [displaysize[0]/2,displaysize[1]/2]
p1bullets = []
p1bulletcooldown = 0

p2size = [30, 50]
p2speed = 4
p2pos = [displaysize[0]/3, displaysize[1]/3]
p2bullets = []
p2bulletcooldown = 0

# Bullet Values
bulletsize = 5
bulletspeed = 10

# Displaying Text
font = pygame.font.Font('freesansbold.ttf', 32)
def message (msg,colour,x,y):
    mesg = font.render(msg, True, colour)
    dis.blit(mesg, [x, y])
def move_player(speed, position, joystick):
    position[0] += joystick[0] * speed
    position[1] += joystick[1] * speed
    if position[0] > displaysize[0] - p1size[0]:
        position[0] = displaysize[0] - p1size[0]
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

#Move entities
    p1pos = move_player(p1speed, p1pos, joystick)
    p2pos = move_player(p2speed, p2pos, keycontrols)
    if keys[pygame.K_SPACE] and p1bulletcooldown == 0:
        bulletposition = [p1pos[0]+p1size[0]/2,p1pos[1] + p1size[1]/2]
        p1bullets.append([bulletposition,0.8])
        p1bulletcooldown = 0.25

    if keys[pygame.K_RSHIFT] and p2bulletcooldown == 0:
        bulletposition = [p2pos[0] + p2size[0]/2, p2pos[1] + p2size[1]/2]
        p2bullets.append([bulletposition, 0.8])
        p2bulletcooldown = 0.25

    # Visual output
    dis.fill(black)
    pygame.draw.rect(dis, red, [p1pos[0], p1pos[1], p1size[0], p1size[1]])
    pygame.draw.rect(dis, blue, [p2pos[0], p2pos[1], p2size[0], p2size[1]])

    for bullet in p1bullets:
        new_pos = move_bullet(bulletspeed,bullet[0],bullet[1])
        pygame.draw.circle(dis, white,new_pos, bulletsize )

    for bullet in p2bullets:
        new_pos = move_bullet(bulletspeed, bullet[0], bullet[1])
        pygame.draw.circle(dis, white, new_pos, bulletsize)


    pygame.display.update()
    fps.tick(60)
pygame.quit()
quit()