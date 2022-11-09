import pygame
from time import sleep
import random

pygame.init()
dis = pygame.display.set_mode((800, 600))
pygame.display.update()
pygame.display.set_caption("Dodge")
game_over = False

# colours
blue = (0, 0, 255)
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
yellow = (255,255,0)

fps = 60
# starting position and display
disx = 800
disy = 600
dis = pygame.display.set_mode((disx, disy))

def getrandx(sizex):
    return (random.randint(0,disx-sizex))
def getrandy(sizey):
    return (random.randint(0,disy-sizey))

enemysizex = 30
enemysizey = 30
enemyspeed = 13
numenemy = 1

psizex = 30
psizey = 50
pspeed = 15
plives = 3
pcooldown = 0
x = disx/2
y = disy/2

clock = pygame.time.Clock()
timer = 10
font = pygame.font.Font('freesansbold.ttf', 32)

def check_x(x,psizex):
    if (x + psizex > disx):
        x = disx - psizex
    if (x < 0):
        x = 0
    return x

def check_y(y,psizey):
    if (y + psizey > disy):
        y = disy - psizey
    if (y < 0):
        y = 0
    return y

def message (msg,colour,x,y):
    mesg = font.render(msg, True, colour)
    dis.blit(mesg, [x, y])

while not game_over:
    pspeed = 6
    if pcooldown > 0:
        pcooldown -= (1/fps)
    if pcooldown < 0:
        pcooldown = 0
    # Closes window if you press the X button
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LSHIFT]:
        pspeed /= 2
    if keys[pygame.K_SPACE] and pcooldown == 0:
        pspeed = 200
        pcooldown = 0.6
    if keys[pygame.K_a]:
        x += -pspeed
        if keys[pygame.K_s] or keys[pygame.K_w]:
            x += 0.414 * pspeed
        x = check_x(x, psizex)
    if keys[pygame.K_d]:
        x += pspeed
        if keys[pygame.K_s] or keys[pygame.K_w]:
            x += 0.414 * -pspeed
        x = check_x(x, psizex)
    if keys[pygame.K_w]:
        y += -pspeed
        if keys[pygame.K_d] or keys[pygame.K_a]:
            y += 0.414 * pspeed
        y = check_y(y,psizey)
    if keys[pygame.K_s]:
        y += pspeed
        if keys[pygame.K_d] or keys[pygame.K_a]:
            y += 0.414 * -pspeed
        y = check_y(y,psizey)

    dis.fill(black)
    pygame.draw.rect(dis, red, [x, y, psizex, psizey])
    pygame.display.update()
    sleep(1/fps)
pygame.quit()
quit()
