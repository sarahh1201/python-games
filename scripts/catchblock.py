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

paddle = pygame.Rect(W // 2 - 60, H - 20, 120, 10)
block = pygame.Rect(random.randint(0, W - 20), 0, 20, 20)
b_speed = 5
score = 0

# Show start screen
start_screen = True
while start_screen:
    screen.fill(BLK)
    game_start = font.render("Press SPACE to start", True, WHT)
    screen.blit(game_start, (W // 2 - 150, H // 2))
    pygame.display.flip()

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif e.type == pygame.KEYDOWN:
            if e.key == pygame.K_SPACE:
                start_screen = False
            elif e.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

# Game loop
run = True
while run:
    screen.fill(BLK)

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.left > 0:
        paddle.move_ip(-8, 0)
    if keys[pygame.K_RIGHT] and paddle.right < W:
        paddle.move_ip(8, 0)

    # Move block
    block.y += b_speed

    # Block caught
    if block.colliderect(paddle):
        block.y = 0
        block.x = random.randint(0, W - 20)
        score += 1
        b_speed += 0.5

    # Block missed
    if block.y > H:
        game_over = font.render(f"Game Over! Final Score: {score}", True, RED)
        screen.blit(game_over, (W // 2 - 150, H // 2))
        pygame.display.flip()
        pygame.time.wait(2000)
        run = False

    # Draw
    pygame.draw.rect(screen, WHT, paddle)
    pygame.draw.rect(screen, BLU, block)
    score_text = font.render(f"Score: {score}", True, WHT)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(60)
