import pygame
import random
import sys

pygame.init()
W, H = 600, 600
screen = pygame.display.set_mode((W, H), pygame.RESIZABLE)
pygame.display.set_caption("Catch the Falling Blocks")

WHT, BLU, RED, BLK = (255, 255, 255), (0, 200, 255), (255, 0, 0), (0, 0, 0)

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

block = pygame.Rect(W // 2 - 60, H - 20, 20, 20)

runnung = True
while runnung:
    screen.fill(BLK)

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and block.left > 0:
        block.move_ip(-8, 0)
    if keys[pygame.K_RIGHT] and block.right < W:
        block.move_ip(8, 0)
    if keys[pygame.K_UP] and block.top > 0:
        block.move_ip(0, -8)
    if keys[pygame.K_DOWN] and block.bottom < H:
        block.move_ip(0, 8)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        runnung = False
        
    pygame.draw.rect(screen, WHT, block)
    pygame.display.flip()
    clock.tick(60)
