import pygame
import random

pygame.init()
width = 1000
height = 500
screen = pygame.display.set_mode((width, height))
red = 255, 0, 0
white = 255, 255, 255
black = 0, 0, 0
green = 0, 255, 0
color_1 = 100, 120, 126

x = 0
y = 0
moveX = random.randint(0,5)
moveY = random.randint(0,5)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    screen.fill(white)
    # screen,color, [x,y,width,height]
    # pygame.draw.rect(screen,red,[x,y,50,50])

    pygame.draw.circle(screen, red, [x,y], 50)
    x += moveX
    y += moveY

    if x > width - 50:
        moveX = random.randint(-5, 0)
    elif x < 50:
        moveX = random.randint(0, 5)
    elif y > height - 50:
        moveY = random.randint(-5, 0)
    elif y < 50:
        moveY = random.randint(0, 5)

    pygame.display.update()