import pygame

pygame.init()

WIDTH = 800
HEIGHT = 600
RED = (255, 0, 0)

window = pygame.display.set_mode((WIDTH,HEIGHT))

pygame.display.set_mode((800, 600))


class Player():
    x = 10
    y = 10
    width = 50
    height = 50
    speed = 5

run = True
while run:
    pygame.time.delay(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keyPressed = pygame.key.get_pressed()

    if keyPressed[pygame.K_a] and Player.x > 0:
        Player.x -= Player.speed
    if keyPressed[pygame.K_d] and Player.x < WIDTH - Player.width:
        Player.x += Player.speed
    if keyPressed[pygame.K_w] and Player.y > 0:
        Player.y -= Player.speed 
    if keyPressed[pygame.K_s] and Player.y < HEIGHT - Player.width: 
        Player.y += Player.speed

    window.fill((0, 0, 0))
    pygame.draw.rect(window, RED, (Player.x, Player.y, Player.width, Player.height))
    pygame.display.update()

pygame.quit()