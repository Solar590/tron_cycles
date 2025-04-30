import pygame
pygame.init()

WIDTH = 600
LENGTH = 800

display = pygame.display.set_mode((WIDTH, LENGTH))
pygame.display.set_caption("Tron Cycles")

cellsize = 20

sx = 300
sy = 400

ix = 0
iy = 0

score = 0

tron = pygame.draw.rect(display, "blue", (sx, sy, 20, 20))

FPS = 20

clock = pygame.time.Clock()

running = True

body = []

while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                ix = 0
                iy = -20
            if event.key == pygame.K_DOWN:
                ix = 0
                iy = +20
            if event.key == pygame.K_RIGHT:
                iy = 0
                ix = +20
            if event.key == pygame.K_LEFT:
                iy = 0
                ix = -20
    sx = sx+ix
    sy = sy+iy
    pos = (sx, sy, 20, 20)
    body.append(pos)
    display.fill("black")
    for parts in body:
        pygame.draw.rect(display, "darkblue", parts)
    tron = pygame.draw.rect(display, "blue", pos)
    pygame.display.update()
    clock.tick(30)
pygame.quit()