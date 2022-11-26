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

# display
displaysize = [800,600]
dis = pygame.display.set_mode((displaysize[0], displaysize[1]))
startup_screen = True

fps = 60

# Player Values
p1size = [30,50]
p1speed = [10,10]
p1pos = [displaysize[0]/2,displaysize[1]/2]

# Displaying Text
font = pygame.font.Font('freesansbold.ttf', 32)
def message (msg,colour,x,y):
    mesg = font.render(msg, True, colour)
    dis.blit(mesg, [x, y])
def move_player(speed, position, joystick):

while not game_over:

    #Visual output
    dis.fill(black)
    pygame.draw.rect(dis, red, [x, y, psizex, psizey])
    pygame.display.update()

    # Closes Window if X is pressed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    keys = pygame.key.get_pressed()

    # Visual output
    dis.fill(black)
    pygame.draw.rect(dis, red, [x, y, psizex, psizey])
    pygame.display.update()

pygame.quit()
quit()
