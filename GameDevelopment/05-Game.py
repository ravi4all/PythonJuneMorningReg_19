import pygame
pygame.init()

width,height = 1000,500

screen = pygame.display.set_mode((width, height))

red = 255,0,0
white = 255,255,255
black = 0,0,0

# rect_1 = pygame.Rect(0,0,50,50)
surface = pygame.Surface((200,200))
surface.fill(red)
rect = surface.get_rect()
rect.center = width/2,height/2

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    screen.fill(white)

    # pygame.draw.rect(surface, red,rect)
    screen.blit(surface, (rect.x, rect.y))

    pygame.draw.rect(surface,black,[0,0,50,50])
    pygame.display.update()