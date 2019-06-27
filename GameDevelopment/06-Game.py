import pygame
pygame.init()

width, height = 1000,500

screen = pygame.display.set_mode((width, height))
red = 255,0,0
white = 255,255,255
black = 0,0,0
green = 0,255,0
color_1 = 100,120,126

x = 0
y = 0
moveX = 0
moveY = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                moveX = 1
                moveY = 0
            elif event.key == pygame.K_LEFT:
                moveX = -1
                moveY = 0
            elif event.key == pygame.K_DOWN:
                moveY = 1
                moveX = 0
            elif event.key == pygame.K_UP:
                moveY = -1
                moveX = 0
        elif event.type == pygame.KEYUP:
            moveX = 0
            moveY = 0

    screen.fill(white)
    pygame.draw.rect(screen,red,[x,y,50,50])
    x += moveX
    y += moveY

    if x > width - 50:
        moveX = -1
    elif x < 0:
        moveX = 1
    elif y > height - 50:
        moveY = -1
    elif y < 0:
        moveY = 1

    pygame.display.update()