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
green = (34,139,34)

# display
displaysize = [800,600]
dis = pygame.display.set_mode((displaysize[0], displaysize[1]))
startup_screen = True
backgroundimage = pygame.image.load(os.path.join('venv', 'background3.png'))
background = pygame.transform.scale(backgroundimage, displaysize)
# Player Values
p1size = 25
p1speed = 4
p1rotation = 0
p1pos = [displaysize[0]/2,displaysize[1]/2]
p1bullets = []
p1bulletcooldown = 0
p1angle = 0
p1lives = 3
p1score = 0
p1image = pygame.image.load(os.path.join('venv', 'p1Sprite.png'))
p1sprite = pygame.transform.scale(p1image, [2.5 *p1size, 2.5 *p1size])



p2size = 25
p2speed = 4
p2rotation = 0
p2pos = [0, displaysize[1]/3]
p2bullets = []
p2bulletcooldown = 0
p2angle = 0
p2lives = 3
p2score = 0
p2image = pygame.image.load(os.path.join('venv', 'p2image.gif'))
p2sprite = pygame.transform.scale(p2image, [2*p2size, 2*p2size])

tree = pygame.image.load(os.path.join('venv', 'tree1.png'))
# Bullet Values
bulletsize = 5
bulletspeed = 10


# Displaying Text
font = pygame.font.Font('freesansbold.ttf', 32)
everyother = True
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
    player = pygame.draw.circle(dis, red, position, size)
    for o in oblist:
        if pygame.Rect.colliderect(player,o):
            position[1] -= joystick[1] * speed

    if position[0] > displaysize[0] - size:
        position[0] = displaysize[0] - size
    if position[0] < 0 + size:
        position[0] = 0 + size
    if position[1] > displaysize[1] - size:
        position[1] = displaysize[1] - size
    if position[1] < 0 + size:
        position[1] = 0 + size
    return position

def move_bullet(speed, position, angle):
    position[0] += speed * cos(angle)
    position [1] += speed * sin(angle)
    return position

def getangle(joystick,angle):
    if joystick == [0,0]:
        return angle
    elif joystick[0] == 0:
        if joystick[1] < 0:
            angle = pi*1.5
        elif joystick[1] > 0:
            angle = pi/2
    elif joystick[1] == 0:
        if joystick[0] > 0:
            angle = 0
        elif joystick[0] < 0:
            angle = pi
    elif joystick[0] > 0:
        angle = atan(joystick[0]/joystick[1])
    elif joystick[0] < 0:
        angle = pi + (atan(joystick[0] / joystick[1]))

    return angle


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
    if everyother == True:
        joystick = [0, 0]
        if keys[pygame.K_w]:
            joystick[1] = -1
        elif keys[pygame.K_s]:
            joystick[1] = 1
        if keys[pygame.K_a]:
            joystick[0] = -1
        elif keys[pygame.K_d]:
            joystick[0] = 1

        #joystick[0] = (joystick_get_x())
        #joystick[1] = (joystick_get_y())
    else:
        everyother = False

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
    dis.blit(background, (0,0))
    o1 = pygame.draw.rect(dis, yellow, [displaysize[0] / 3, displaysize[1] / 3, 35, 35])
    o2 = pygame.draw.rect(dis, yellow, [displaysize[0] * 2 / 3, displaysize[1] / 3, 30, 30])
    o3 = pygame.draw.rect(dis, yellow, [displaysize[0] / 3, displaysize[1] * 2 / 3, 25, 25])
    o4 = pygame.draw.circle(dis, green, [displaysize[0] * 2 / 3, displaysize[1] * 2 / 3], 45,1)
    o4sprite = pygame.transform.scale(tree,[182,130])
    o5 = pygame.draw. circle(dis, green, [displaysize[0] * 1 / 6, displaysize[1] * 1 / 6], 35, 1)
    o5sprite = pygame.transform.scale(tree,[145,105])
    o6 = pygame.draw.rect(dis, yellow, [displaysize[0] * 5 / 6, displaysize[1] * 5 / 6, 30, 30])
    o7 = pygame.draw.rect(dis, yellow, [displaysize[0] * 1 / 6, displaysize[1] * 5 / 6, 25, 25])
    o8 = pygame.draw.rect(dis, yellow, [displaysize[0] * 5 / 6, displaysize[1] * 1 / 6, 20, 20])
    o9 = pygame.draw.rect(dis, yellow, [displaysize[0] * 1 / 6, displaysize[1] * 1 / 2, 20, 20])
    o10 = pygame.draw.rect(dis, yellow, [displaysize[0] * 1 / 2, displaysize[1] * 1 / 6, 40, 40])
    o11 = pygame.draw.rect(dis, yellow, [displaysize[0] * 1 / 2, displaysize[1] * 5 / 6, 30, 30])
    o12 = pygame.draw.rect(dis, yellow, [displaysize[0] * 5 / 6, displaysize[1] * 1 / 2, 25, 25])
    o13 = pygame.draw.rect(dis, yellow, [displaysize[0] * 1 / 2, displaysize[1] * 6 / 10, 35, 35])
    oblist = [o1, o2, o3, o4, o5, o6, o7, o8, o9, o10, o11, o12, o13]

    p1 = pygame.draw.circle(dis, black, p1pos, p1size,1)
    p1rotation = (getangle(joystick,p1rotation/57.2958) * 57.2958)
    p1sprite = pygame.transform.scale(p1image, [2.5 * p1size, 2.5 * p1size])
    p1sprite = pygame.transform.rotate(p1sprite,360 - p1rotation)

    p2 = pygame.draw.circle(dis, black, p2pos, p2size,1)
    p2rotation = (getangle(keycontrols, p2rotation / 57.2958) * 57.2958)
    p2sprite = pygame.transform.scale(p2image, [2*p2size, 2*p2size])
    p2sprite = pygame.transform.rotate(p2sprite, 360 - p2rotation)

    dis.blit(p1sprite, (p1.x-2,p1.y - 10))
    dis.blit(p2sprite, (p2.x+1, p2.y-5))
    dis.blit(o5sprite, (o5.x-40, o5.y-20))
    dis.blit(o4sprite, (o4.x-48, o4.y-24))


    for bullet in p1bullets:
        new_pos = move_bullet(bulletspeed, bullet[0], bullet[1])
        b = pygame.draw.circle(dis, white, new_pos, bulletsize)
        if pygame.Rect.contains(p2,b):
            p2lives -= 1
            p1bullets.remove(bullet)
        else:
            for obstacle in oblist:
                if pygame.Rect.colliderect(obstacle,b):
                    p1bullets.remove(bullet)
    for bullet in p2bullets:
        new_pos = move_bullet(bulletspeed, bullet[0], bullet[1])
        b = pygame.draw.circle(dis, white, new_pos, bulletsize)
        if pygame.Rect.contains(p1,b):
            p1lives -= 1
            p2bullets.remove(bullet)
        for obstacle in oblist:
            if pygame.Rect.colliderect(obstacle,b):
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

    #Bullets
    p1angle = getangle(joystick,p1angle)
    p2angle = getangle(keycontrols,p2angle)

    if keys[pygame.K_SPACE] and p1bulletcooldown == 0:
        bulletposition = [p1pos[0], p1pos[1]]
        p1bullets.append([bulletposition, p1angle])
        p1bulletcooldown = 0.25

    if keys[pygame.K_RSHIFT] and p2bulletcooldown == 0:
        bulletposition = [p2pos[0], p2pos[1]]
        p2bullets.append([bulletposition, p2angle])
        p2bulletcooldown = 0.25

    fps.tick(60)
pygame.quit()
quit()