import pygame
from engi1020.arduino.api import *
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
p1speed = 10
p1pos = [displaysize[0]/2,displaysize[1]/2]

# Displaying Text
font = pygame.font.Font('freesansbold.ttf', 32)
def message (msg,colour,x,y):
    mesg = font.render(msg, True, colour)
    dis.blit(mesg, [x, y])
def move_player(speed, position, joystick):
    position[0] += joystick[0] * speed
    position[1] += joystick[1] * speed
while not game_over:

    # Closes Window if X is pressed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    keys = pygame.key.get_pressed()

    joystick = analog_read(2)
    print(joystick)
    # Visual output
    dis.fill(black)
    pygame.draw.rect(dis, red, [p1pos[0], p1pos[1], p1size[0], p1size[1]])
    pygame.display.update()

pygame.quit()
quit()
