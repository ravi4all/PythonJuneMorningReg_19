import pygame
import random
pygame.init()

width, height = 1000,500

screen = pygame.display.set_mode((width, height))
red = 255,0,0
white = 255,255,255
black = 0,0,0
green = 0,255,0
color_1 = 100,120,126

frog = pygame.image.load("assets/frog.png")
frogWidth = frog.get_width()
frogHeight = frog.get_height()
frogX = random.randint(0,width - frogWidth)
frogY = random.randint(0,height - frogHeight)

backgroundMusic = pygame.mixer.Sound('assets/bg_music.wav')
backgroundMusic.play(-1)

coinSound = pygame.mixer.Sound('assets/point.wav')

x = 0
y = 0
moveX = 0
moveY = 0

snakew = 50
snakeLength = 1
snakeList = []

def snake(snakeList):
    for i in range(len(snakeList)):
        pygame.draw.rect(screen, red, [snakeList[i][0],
                                       snakeList[i][1],
                                       50,50])

def score(count):
    font = pygame.font.SysFont(None, 30)
    text = font.render("Score : {}".format(count), True, black)
    screen.blit(text, (100,10))

FPS = 100
clock = pygame.time.Clock()

count = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                moveX = 5
                moveY = 0
            elif event.key == pygame.K_LEFT:
                moveX = -5
                moveY = 0
            elif event.key == pygame.K_DOWN:
                moveY = 5
                moveX = 0
            elif event.key == pygame.K_UP:
                moveY = -5
                moveX = 0

    screen.fill(white)

    screen.blit(frog,(frogX, frogY))
    snake_rect = pygame.draw.rect(screen,red,[x,y,snakew,50])

    frog_rect = pygame.Rect(frogX, frogY, frogWidth, frogHeight)
    # pygame.draw.rect(screen, red, frog_rect)

    x += moveX
    y += moveY

    snakeHead = []
    snakeHead.append(x)
    snakeHead.append(y)

    snakeList.append(snakeHead)

    if len(snakeList) > snakeLength:
        del snakeList[0]
    # print(snakeList)
    snake(snakeList)

    if frog_rect.colliderect(snake_rect):
        frogX = random.randint(0, width - frogWidth)
        frogY = random.randint(0, height - frogHeight)
        snakeLength += 6
        FPS += 5
        coinSound.play()
        count += 1

    score(count)

    if x > width:
        x = -50
    elif x < -50:
        x = width
    elif y > height:
        y = -50
    elif y < -50:
        y = height

    pygame.display.update()
    clock.tick(FPS)