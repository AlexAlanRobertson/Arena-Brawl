import pygame

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

p1size = [30,50]
p1speed = [10,10]
p1lives = 3
p1cooldown = 0
p1pos = [disx/1.5,disy/2]

p2size = [30,50]
p2speed = [10,10]
p2lives = 3
p2cooldown = 0
p2pos = [disx/4,disy/2]

clock = pygame.time.Clock()
timer = 10
font = pygame.font.Font('freesansbold.ttf', 32)
def message (msg,colour,x,y):
    mesg = font.render(msg, True, colour)
    dis.blit(mesg, [x, y])

while not game_over:
    # Closes window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    keys = pygame.key.get_pressed()

    dis.fill(black)
    pygame.draw.rect(dis, red, [p1pos[0], p1pos[1], p1size[0], p1size[1]])
    pygame.draw.rect(dis, blue, [p2pos[0], p2pos[1], p2size[0], p2size[1]])
    pygame.display.update()

#PLAYER ONE MOVEMENT AND ABLIITY
    if keys[pygame.K_SPACE] and p1cooldown == 0:
        p1speed[0] = 200
        p1speed[1]= 200
    if keys[pygame.K_a]:
        p1pos[0] += -p1speed[0]
        if keys[pygame.K_s] or keys[pygame.K_w]:
            p1pos[0] += 0.414 * p1speed
        p1pos[0] = check_x(p1pos[0], p1sizex)
    if keys[pygame.K_d]:
        p1pos[0] += p1speed
        if keys[pygame.K_s] or keys[pygame.K_w]:
            p1pos[0] += 0.414 * -p1speed
        p1pos[0] = check_x(p1pos[0], p1sizex)
    if keys[pygame.K_w]:
        p1pos[1] += -p1speed
        if keys[pygame.K_d] or keys[pygame.K_a]:
            p1pos[1] += 0.414 * p1speed
        p1pos[1] = check_y(y1,p1sizey)
    if keys[pygame.K_s]:
        p1pos[1] += p1speed
        if keys[pygame.K_d] or keys[pygame.K_a]:
            y1 += 0.414 * -p1speed
        p1pos[1] = check_y(y1,p1sizey)

#PLAYER TWO MOVEMENT AND ABILITYs
    if keys[pygame.K_LEFT]:
        x2 += -p2speed
        if keys[pygame.K_DOWN] or keys[pygame.K_UP]:
            x2 += 0.414 * p2speed
        x2 = check_x(x2, p2sizex)
    if keys[pygame.K_RIGHT]:
        x2 += p2speed
        if keys[pygame.K_s] or keys[pygame.K_w]:
            x2 += 0.414 * -p2speed
        x2 = check_x(x2, p2sizex)
    if keys[pygame.K_UP]:
        y2 += -p2speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_LEFT]:
            y2 += 0.414 * p2speed
        y2 = check_y(y2,p2sizey)
    if keys[pygame.K_DOWN]:
        y2 += p2speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_LEFT]:
            y2 += 0.414 * -p2speed
        y2 = check_y(y2,p2sizey)

pygame.quit()
quit()