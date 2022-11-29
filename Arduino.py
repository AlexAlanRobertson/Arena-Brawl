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
sand = (194,178,128)

# display
displaysize = [800,600]
dis = pygame.display.set_mode((displaysize[0], displaysize[1]))
backgroundimage = pygame.image.load(os.path.join('venv', 'background3.png'))
background = pygame.transform.scale(backgroundimage, displaysize)
# Player Values
p1size = 25
p1speed = 4
p1rotation = 180
p1pos = [750, displaysize[1] / 2]
p1bullets = []
p1bulletcooldown = 0
p1bulletangle = pi
p1lives = 3
p1score = 0
p1image = pygame.image.load(os.path.join('venv', 'p1Sprite.png'))



p2size = 25
p2speed = 4
p2rotation = 0
p2pos = [10,displaysize[1]/2]
p2bullets = []
p2bulletcooldown = 0
p2bulletangle = 0
p2lives = 3
p2score = 0
p2image = pygame.image.load(os.path.join('venv', 'p2image.gif'))

tree = pygame.image.load(os.path.join('venv', 'tree1.png'))
barrel = pygame.image.load(os.path.join('venv', 'barrel.png'))
# Bullet Values
bulletsize = 5
bulletspeed = 10

o1 = pygame.draw.circle(dis, green, [displaysize[0] / 3, displaysize[1] / 3], 25, 1)
o1sprite = pygame.transform.scale(barrel, [60, 60])
o2 = pygame.draw.circle(dis, green, [displaysize[0] * 2 / 3, displaysize[1] / 3], 25, 1)
o2sprite = pygame.transform.scale(barrel, [60, 60])
o3 = pygame.draw.circle(dis, green, [displaysize[0] / 3, displaysize[1] * 2 / 3], 45, 1)
o3sprite = pygame.transform.scale(tree, [200, 150])
o4 = pygame.draw.circle(dis, green, [displaysize[0] * 2 / 3, displaysize[1] * 2 / 3], 45, 1)
o4sprite = pygame.transform.scale(tree, [182, 130])
o5 = pygame.draw.circle(dis, green, [displaysize[0] * 1 / 6, displaysize[1] * 1 / 6], 35, 1)
o5sprite = pygame.transform.scale(tree, [145, 105])
o6 = pygame.draw.circle(dis, green, [displaysize[0] * 5 / 6, displaysize[1] * 5 / 6], 30, 1)
o6sprite = pygame.transform.scale(tree, [155, 115])
o7 = pygame.draw.circle(dis, green, [displaysize[0] * 1 / 6, displaysize[1] * 5 / 6], 25, 1)
o7sprite = pygame.transform.scale(barrel, [60, 60])
o8 = pygame.draw.circle(dis, green, [displaysize[0] * 5 / 6, displaysize[1] * 1 / 6], 25, 1)
o8sprite = pygame.transform.scale(barrel, [60, 60])
o9 = pygame.draw.circle(dis, green, [displaysize[0] * 1 / 6, displaysize[1] * 1 / 2], 30, 1)
o9sprite = pygame.transform.scale(barrel, [60, 60])
o10 = pygame.draw.circle(dis, green, [displaysize[0] * 1 / 2, displaysize[1] * 1 / 6], 40, 1)
o10sprite = pygame.transform.scale(tree, [190, 140])
o11 = pygame.draw.circle(dis, green, [displaysize[0] * 1 / 2, displaysize[1] * 5 / 6], 25, 1)
o11sprite = pygame.transform.scale(barrel, [60, 60])
o12 = pygame.draw.circle(dis, green, [displaysize[0] * 5 / 6, displaysize[1] * 1 / 2], 25, 1)
o12sprite = pygame.transform.scale(barrel, [60, 60])
o13 = pygame.draw.circle(dis, green, [displaysize[0] * 1 / 2, displaysize[1] * 6 / 10], 25, 1)
o13sprite = pygame.transform.scale(barrel, [60, 60])
oblist = [o1, o2, o3, o4, o5, o6, o7, o8, o9, o10, o11, o12, o13]

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

startup_screen = True
buttonpressed = False
message_displayed = True


while startup_screen == True and game_over == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    buttonpressed = digital_read(6)
    if buttonpressed == True:
        startup_screen = False
        buzzer_frequency(5, 60)
        sleep(1)
        buzzer_stop(5)
        sleep(1)
        buzzer_frequency(5, 60)
        sleep(1)
        buzzer_stop(5)
        sleep(1)
        buzzer_frequency(5, 60)
        sleep(1)
        buzzer_stop(5)

    dis.fill(black)
    if message_displayed == True:
        message("Hold the Button to Start the Game", white, 140, displaysize[1]/2)
        pygame.display.update()
        sleep(0.8)
        message_displayed = False
    else:
        pygame.display.update()
        sleep(0.8)
        message_displayed = True


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
        everyother = False
    else:
        everyother = True
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
    dis.blit(background, (0,0))

    p1 = pygame.draw.circle(dis, sand, p1pos, p1size, 1)
    p1rotation = (getangle(joystick, p1rotation / 57.2958) * 57.2958)
    p1sprite = pygame.transform.scale(p1image, [4 * p1size, 4 * p1size])
    p1sprite = pygame.transform.rotate(p1sprite, 360 - p1rotation)

    p2 = pygame.draw.circle(dis, sand, p2pos, p2size, 1)
    p2rotation = (getangle(keycontrols, p2rotation / 57.2958) * 57.2958)
    p2sprite = pygame.transform.scale(p2image, [3 * p2size, 3 * p2size])
    p2sprite = pygame.transform.rotate(p2sprite, 360 - p2rotation)

    if int(p1rotation % 90) == 0:
        dis.blit(p1sprite, (p1.x-p1size,p1.y-p1size))
    else:
        dis.blit(p1sprite, (p1.x - 2*p1size, p1.y - 2*p1size))

    if keycontrols[0] == 0 or keycontrols[1] == 0:
        dis.blit(p2sprite, (p2.x-p2size/2, p2.y-p2size/2))
    else:
        dis.blit(p2sprite, (p2.x - p2size, p2.y - p2size))

    dis.blit(o3sprite, [o3.x - 55, o3.y - 35])
    dis.blit(o10sprite, [o10.x - 55, o10.y - 35])
    dis.blit(o6sprite, [o6.x - 45, o6.y - 25])
    dis.blit(o7sprite, [o7.x - 3, o7.y - 5])
    dis.blit(o2sprite, [o2.x - 3, o2.y - 5])
    dis.blit(o1sprite, (o1.x - 3, o1.y - 5))
    dis.blit(o8sprite, (o8.x - 3, o8.y - 5))
    dis.blit(o9sprite, [o9.x, o9.y])
    dis.blit(o11sprite, [o11.x - 3, o11.y - 5])
    dis.blit(o12sprite, [o12.x - 3, o12.y - 5])
    dis.blit(o13sprite, [o13.x - 3, o13.y - 5])
    dis.blit(o5sprite, (o5.x-40, o5.y-20))
    dis.blit(o4sprite, (o4.x-48, o4.y-24))




    for bullet in p1bullets:
        new_pos = move_bullet(bulletspeed, bullet[0], bullet[1])
        b = pygame.draw.circle(dis, white, new_pos, bulletsize)
        if pygame.Rect.colliderect(p2,b):
            p2lives -= 1
            p1bullets.remove(bullet)
        else:
            for obstacle in oblist:
                if pygame.Rect.colliderect(obstacle,b):
                    p1bullets.remove(bullet)
    for bullet in p2bullets:
        new_pos = move_bullet(bulletspeed, bullet[0], bullet[1])
        b = pygame.draw.circle(dis, white, new_pos, bulletsize)
        if pygame.Rect.colliderect(p1,b):
            p1lives -= 1
            p2bullets.remove(bullet)
        else:
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
        p2lives = 3
        p1lives = 3
        p1pos = [750, displaysize[1] / 2]
        p2pos = [10,displaysize[1]/2]
    elif p2lives == 0:
        sleep(1)
        p1score += 1
        p1lives = 3
        p2lives = 3
        p1pos = [750, displaysize[1]/2]
        p2pos = [10, displaysize[1] / 2]

    if p1score == 5:
        dis.fill(black)
        message("Player One Wins", red, displaysize[0]/3, displaysize[1]/2)
        pygame.display.update()
        oled_print('P1 Wins!')
        sleep(3)
        game_over = True
    if p2score == 5:
        dis.fill(black)
        message("Player Two Wins", blue, displaysize[0]/3, displaysize[1]/2)
        pygame.display.update()
        oled_print('P2 Wins!')
        sleep(3)
        game_over = True

        # Move entities
    p1pos = move_player(p1speed, p1pos, joystick, p1, p1size)
    p2pos = move_player(p2speed, p2pos, keycontrols, p2,p2size)

    #bullets
    p1bulletangle = getangle(joystick, p1bulletangle)
    p2bulletangle = getangle(keycontrols, p2bulletangle)
    if keys[pygame.K_SPACE] and p1bulletcooldown == 0:
        bulletposition = [p1pos[0], p1pos[1]]
        p1bullets.append([bulletposition, p1bulletangle])
        p1bulletcooldown = 0.25

    if keys[pygame.K_RSHIFT] and p2bulletcooldown == 0:
        bulletposition = [p2pos[0], p2pos[1]]
        p2bullets.append([bulletposition, p2bulletangle])
        p2bulletcooldown = 0.25
    fps.tick(60)
pygame.quit()
quit()