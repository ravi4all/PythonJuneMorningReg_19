import pygame
pygame.init()

width,height = 1000,500
screen = pygame.display.set_mode((width, height))
red = 255,0,0
white = 255,255,255
black = 0,0,0
green = 0,255,0
blue = 0,0,255
color_1 = 100,120,126

def game():

    barWidth = 160
    barHeight = 15
    barX = (width // 2) - (barWidth // 2)
    barY = height - barHeight - 10
    moveX = 0

    ballRadius = 8
    ballY = barY - ballRadius
    moveBallX = 0
    moveBallY = 0
    moveBall = False

    brickWidth = 100
    brickHeight = 25

    brickList = []
    for row in range(5):
        for col in range(10):
            brickList.append(pygame.Rect(col*(brickWidth + 5), row*(brickHeight+5), brickWidth, brickHeight))

    while True:
        if not moveBall:
            ballX = barX + barWidth // 2
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    moveX = 1
                elif event.key == pygame.K_LEFT:
                    moveX = -1
                elif event.key == pygame.K_SPACE:
                    moveBallX = 1
                    moveBallY = -1
                    moveBall = True
            elif event.type == pygame.KEYUP:
                moveX = 0

        screen.fill(white)

        barRect = pygame.draw.rect(screen, black, (barX, barY, barWidth, barHeight))
        pygame.draw.circle(screen, red, [ballX, ballY], ballRadius)
        ballRect = pygame.Rect(ballX,ballY,ballRadius,ballRadius)

        ballX += moveBallX
        ballY += moveBallY

        for i in range(len(brickList)):
            pygame.draw.rect(screen, blue, brickList[i])

        barX += moveX

        for i in range(len(brickList)):
            if ballRect.colliderect(brickList[i]):
                del brickList[i]
                moveBallY = 1
                break

        if ballY < ballRadius:
            moveBallY = 1
        elif ballY > height + height:
            moveBallX = 0
            moveBallY = 0
            moveBall = False
            ballY = barY - ballRadius
        elif ballX < ballRadius:
            moveBallX = 1
        elif ballX > width - ballRadius:
            moveBallX = -1
        elif ballRect.colliderect(barRect):
            moveBallY = -1


        pygame.display.update()

game()