import pygame
import random
from pygame.locals import *
import time
pygame.init()

width = 1000
height = 500
screen = pygame.display.set_mode((width, height))

red = 255,0,0
white = 255,255,255
yellow = 255,255,0

FPS = 50
clock = pygame.time.Clock()

def homeScreen():
    bg_img = pygame.image.load("bg_img.jpg")
    font = pygame.font.Font("font_2.ttf",50)
    text = font.render("Press SPACE to Start Game", True, yellow)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game()

        screen.blit(bg_img, (0,0))
        screen.blit(text, (200,100))
        pygame.display.update()

def gameOver():
    pass

def timer(seconds):
    font = pygame.font.Font('font_2.ttf', 30)
    text = font.render("Time Left : {}".format(seconds), True, yellow)
    screen.blit(text, (400, 10))

def score(counter):
    font = pygame.font.Font('font_2.ttf',30)
    text = font.render("Score : {}".format(counter), True, yellow)
    screen.blit(text, (10,10))

def bloodPatch(posx, posy):
    bloodPatchImg = pygame.image.load("zombie_blood.png")
    bloodWidth = bloodPatchImg.get_width()
    bloodHeight = bloodPatchImg.get_height()
    while True:
        screen.blit(bloodPatchImg, (posx - bloodWidth/2, posy-bloodHeight/2))
        pygame.display.update()
        # time.sleep(0.1)
        clock.tick(5)
        break

def game():
    gunPointer = pygame.image.load('aim_pointer.png')
    gunPointerWidth = gunPointer.get_width()
    gunPointerHeight = gunPointer.get_height()

    gunImage = pygame.image.load("gun.png")
    gunImageWidth = gunImage.get_width()
    gunImageHeight = gunImage.get_height()
    gunY = height - gunImageHeight
    bgImage = pygame.image.load("background.png")

    gunSound = pygame.mixer.Sound("shot_sound.wav")

    zombieList = []
    for i in range(1, 5):
        zombieList.append(pygame.image.load("zombie_{}.png".format(i)))

    zombieImage = random.choice(zombieList)
    zombieWidth = zombieImage.get_width()
    zombieHeight = zombieImage.get_height()
    zombieX = random.randint(0, width - zombieWidth)
    zombieY = random.randint(0, height - zombieHeight)

    count = 0
    seconds = 20
    # xt = 1
    pygame.time.set_timer(USEREVENT,1000)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == USEREVENT:
                seconds -= 1

            if event.type == pygame.MOUSEBUTTONDOWN:
                gunSound.play()
                if rect_1.colliderect(rect_2):
                    # zombieImage = pygame.transform.scale(zombieImage, (100,100))
                    bloodPatch(posx, posy)
                    zombieImage = random.choice(zombieList)
                    zombieWidth = zombieImage.get_width()
                    zombieHeight = zombieImage.get_height()
                    zombieX = random.randint(0, width - zombieWidth)
                    zombieY = random.randint(0, height - zombieHeight)
                    count += 1


        screen.fill(white)
        posx,posy = pygame.mouse.get_pos()
        screen.blit(bgImage, (0,0))
        screen.blit(zombieImage, (zombieX, zombieY))
        screen.blit(gunPointer, (posx - gunPointerWidth/2, posy - gunPointerHeight/2))
        screen.blit(gunImage, (posx, gunY))

        rect_1 = pygame.Rect(posx - gunPointerWidth/2, posy - gunPointerHeight/2, gunPointerWidth, gunPointerWidth)
        rect_2 = pygame.Rect(zombieX, zombieY, zombieWidth, zombieHeight)

        score(count)
        timer(seconds)

        pygame.display.update()
        clock.tick(FPS)

# game()
homeScreen()