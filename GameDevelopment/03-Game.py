import pygame
pygame.init()

screen = pygame.display.set_mode((1000,500))
red = 255,0,0
white = 255,255,255
black = 0,0,0
green = 0,255,0
color_1 = 100,120,126

screen.fill(color_1)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # screen,color, [x,y,width,height]
    # pygame.draw.rect(screen,white,[0,0,50,50])

    # screen, color, [x,y], radius
    pygame.draw.circle(screen,white,[0,0],50)

    pygame.display.update()