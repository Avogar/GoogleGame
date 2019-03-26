import pygame, random, os, sys
pygame.init()

def dino_jump(t):
    dy = 9*t - 0.123*t**2
    return dy

def draw_dino(run):
    if bum == 1:
        screen.blit(dino_shock,[x_dino, y_dino])
    elif start == 0 or jump == 1:
        screen.blit(dino_standing,[x_dino, y_dino])
    else:
        if run >= 0:
            screen.blit(dino_run1, [x_dino, y_dino])
        else:
            screen.blit(dino_run2, [x_dino, y_dino])
def draw_cloud():
    for i in range(4):
        screen.blit(cloud, [x_cloud[i], y_cloud[i]])
        if start == 1:
            x_cloud[i] -= 1
        if x_cloud[i] <= -70:
            x_cloud[i] = max(x_cloud) + 200
            y_cloud[i] = random.randrange(30,200)

def draw_cactus():
    for i in range(count_cactus):
        screen.blit(cactus_image[cactus[i][4]-1],cactus[i][0:2])
        if start == 1:
            cactus[i][0] -= speed
        if cactus[i][0] <= -1*cactus[i][2]:
            maximum = 0
            for j in range(len(cactus)):
                if maximum < cactus[j][0]:
                    maximum = cactus[j][0]
            x_new = maximum + random.randrange(200 + speed*75,500 + speed*75)
            b = 5
            if speed == 4:
                b = 6
            elif speed == 5:
                b = 7
            elif speed == 6:
                b = 8
            elif speed == 7:
                b = 9
            elif speed >= 8:
                b = 10
            num = random.randrange(1, b)
            if num == 1:
                dx = 36
                dy = 70
            elif num == 2:
                dx = 24
                dy = 51
            elif num == 3:
                dx = 72
                dy = 70
            elif num == 4:
                dx = 50
                dy = 51
            elif num == 5:
                dx = 75
                dy = 51
            elif num == 6:
                dx = 101
                dy = 51
            elif num == 7:
                dx = 145
                dy = 70
            elif num == 8:
                dx = 126
                dy = 51
            elif num == 9:
                dx = 182
                dy = 70
            cactus[i] = [x_new, size[1] - 30 - dy, dx, dy, num]

def draw_dust():
    if len(dust) == 0 or size[0] - dust[len(dust)- 1][0] >= random.randrange(15,60):
        dust.append([size[0], random.randrange(size[1] - 38, size[1] - 1), random.randrange(2,7),2])
    for i in range(len(dust)):
        pygame.draw.rect(screen,color,dust[i])
        if start == 1:
            dust[i][0] -= speed
    if dust[0][0] < 0:
        dust.pop(0)

def bump(s):
    for i in range(len(cactus)):
        if -cactus[i][2]//2 <= cactus[i][0] + 18 - (x_dino + dx_dino//3) <= 2*dx_dino//3 and -cactus[i][3]//2 <= cactus[i][1] + 10 - y_dino <= dy_dino:
            s = 1
    return s
def game_over():
    screen.blit(gameover,[(size[0]-286)/2, (size[1]-98)/2])

def draw_score():
    font = pygame.font.Font(None, 25)
    text = font.render('Score: ' + str(score),True,color)
    screen.blit(text, [5,5])
    if best != 0:
        text = font.render('Best: ' + str(best), True, color)
        screen.blit(text, [5,26])




black = (0,0,0)
white = (255,255,255)
green = (0,255,0)
red = (255,0,0)
blue = (0,0,255)
yellow = (255,255,0)
cyan = (0,255,255)
grey = (190,190,190)
orange = (255,165,0)
brown = (139,69,19)
purple = (160,32,240)
DarkGreen = (0,128,0)
color = (83,83,83)


size = [800,400]
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Google game')

trip = sys.path[0]


dino_standing = pygame.image.load(trip + '/data/standing.png').convert()
dino_standing.set_colorkey(white)
dino_run1 = pygame.image.load(trip + '/data/run1.png').convert()
dino_run1.set_colorkey(white)
dino_run2 = pygame.image.load(trip + '/data/run2.png').convert()
dino_run2.set_colorkey(white)
dino_shock = pygame.image.load(trip + '/data/shock.png').convert()
dino_shock.set_colorkey(white)
cloud = pygame.image.load(trip + '/data/cloud.png').convert()
cloud.set_colorkey(white)
cactus1 = pygame.image.load(trip + '/data/cactus1.png').convert()
cactus1.set_colorkey(white)
cactus2 = pygame.image.load(trip + '/data/cactus2.png').convert()
cactus2.set_colorkey(white)
cactus3 = pygame.image.load(trip + '/data/cactus3.png').convert()
cactus3.set_colorkey(white)
cactus4 = pygame.image.load(trip + '/data/cactus4.png').convert()
cactus4.set_colorkey(white)
cactus5 = pygame.image.load(trip + '/data/cactus5.png').convert()
cactus5.set_colorkey(white)
cactus6 = pygame.image.load(trip + '/data/cactus6.png').convert()
cactus6.set_colorkey(white)
cactus7 = pygame.image.load(trip + '/data/cactus7.png').convert()
cactus7.set_colorkey(white)
cactus8 = pygame.image.load(trip + '/data/cactus8.png').convert()
cactus8.set_colorkey(white)
cactus9 = pygame.image.load(trip + '/data/cactus9.png').convert()
cactus9.set_colorkey(white)
gameover = pygame.image.load(trip + '/data/gameover.png').convert()
gameover.set_colorkey(white)

trip = sys.path[0]

best_open = open(trip + '/data/best.txt', 'r')
best = int(best_open.read())
best_open.close()

cactus_image = [cactus1,cactus2,cactus3,cactus4,cactus5,cactus6,cactus7,cactus8,cactus9]

done2 = True
start = 0

clock = pygame.time.Clock()

while done2:
    done = True
    x_cloud = [size[0] + 200*i for i in range(4)]
    y_cloud = []
    for i in range(4):
        y_cloud.append(random.randrange(30,200))

    dust = []
    score = 0
    jump = 0
    t = 1
    run = 0
    x_dino = 10
    y0 = y_dino = size[1] - 95
    dx_dino = 62
    dy_dino = 65
    count_cactus = 5
    speed = 3
    bum = 0
    cactus = []
    for i in range(count_cactus):
        num = random.randrange(1,5)
        if num == 1:
            dx = 36
            dy = 70
        elif num == 2:
            dx = 24
            dy = 51
        elif num == 3:
            dx = 72
            dy = 70
        elif num == 4:
            dx = 50
            dy = 51
        cactus.append([size[0] + 400*i, size[1] - 30 - dy,dx,dy,num])

    while done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = False
                done2 = False
                best_open = open(trip + '/data/best.txt', 'w')
                best_open.write(str(best))
                best_open.close()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    jump = 1
                    if start == 0:
                        start = 1
                    if bum == 1:
                        done = False
                        bum = 0
                        if score > best:
                            best = score

        if 100 <= score < 250:
            speed = 4
        elif 250 <= score < 550:
            speed = 5
        elif 550 <= score < 1000:
            speed = 6
        elif 1000 <= score < 2000:
            speed = 7
        elif 2000 <= score < 3500:
            speed = 8
        elif 3500 <= score < 5000:
            speed = 9
        elif score >= 5000:
            speed = 10


        if bum == 1: start = 0
        if start == 1 and bum == 0: bum = bump(bum)

        if bum == 0 and start == 1:
            if run == 10:
                score += int(speed*1.5) - 2
                run *= -1
            run += 1

        if jump == 1 and bum == 0:
            y_dino = y0 - dino_jump(t)
            t += 1
            if y_dino >= y0:
                y_dino = y0
                jump = 0
                t = 1

        screen.fill(white)

        pygame.draw.rect(screen,yellow,[0,size[1] - 40,size[0],40])

        pygame.draw.line(screen, color, [0,size[1] - 40], [size[0], size[1] - 40])

        draw_cloud()
        draw_cactus()
        draw_dust()
        draw_dino(run)
        draw_score()

        if bum == 1:
            game_over()

        pygame.display.flip()

        clock.tick(130)

pygame.quit()