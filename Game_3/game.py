import pygame
import random
pygame.init()

width = 1000
height = 500
screen = pygame.display.set_mode((width, height))

red = 255,0,0
white = 255,255,255

gunPointer = pygame.image.load('aim_pointer.png')
gunPointerWidth = gunPointer.get_width()
gunPointerHeight = gunPointer.get_height()

gunImage = pygame.image.load("gun.png")
gunImageWidth = gunImage.get_width()
gunImageHeight = gunImage.get_height()
gunY = height - gunImageHeight
bgImage = pygame.image.load("background.png")

zombieList = []
for i in range(1,5):
    zombieList.append(pygame.image.load("zombie_{}.png".format(i)))

zombieImage = random.choice(zombieList)
zombieWidth = zombieImage.get_width()
zombieHeight = zombieImage.get_height()
zombieX = random.randint(0,width - zombieWidth)
zombieY = random.randint(0,height - zombieHeight)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            print("Mouse Click")

    screen.fill(white)
    posx,posy = pygame.mouse.get_pos()
    screen.blit(bgImage, (0,0))
    screen.blit(zombieImage, (zombieX, zombieY))
    screen.blit(gunPointer, (posx - gunPointerWidth/2, posy - gunPointerHeight/2))
    screen.blit(gunImage, (posx, gunY))

    pygame.display.update()