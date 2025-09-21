import pygame
import random

pygame.init()

# Настройки окна
WIDTH, HEIGHT = 600, 400
fps= 1
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Змейка")
clock = pygame.time.Clock()
snake = pygame.image.load('images/tarzan.jpg')


x, y = WIDTH / 2, HEIGHT / 2

while True:
    pygame.display.update()
    screen.fill((51, 255 , 51))
    screen.blit(snake, (x, y))
    clock.tick(fps)
    
    if x > WIDTH or y > HEIGHT:
        exit()
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                x += 5
            elif event.key == pygame.K_w:
                y -= 5
            elif event.key == pygame.K_s:
                y += 5
            elif event.key == pygame.K_a:
                x -= 5
    
    