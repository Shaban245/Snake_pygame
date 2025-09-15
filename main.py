import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((600, 300))
screen.fill((102, 255, 102))
player = pygame.image.load('images/tarzan.jpg')
keys = pygame.key.get_pressed()
player_x = 20
player_y = 50
pl_speed = 10
while True:
    screen.blit(player, (player_x, player_y))
    
    
    if keys[pygame.K_RIGHT]:
        player_x += pl_speed
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    pygame.display.update()
            