import pygame
from src.Game import Game
from src import constants

pygame.init()

game = Game()





while True:
    pygame.display.update()
    game.screen.fill(game.field.rgb_color)
    game.screen.blit(game.snake.image, (game.snake.x_position, game.snake.y_position))
    game.clock.tick(constants.FPS)
    

    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                game.snake.change_direction(game.snake.dict_direction[constants.rigth])
            elif event.key == pygame.K_w:
                game.snake.change_direction(game.snake.dict_direction[constants.up])
            elif event.key == pygame.K_s:
                game.snake.change_direction(game.snake.dict_direction[constants.down])
            elif event.key == pygame.K_a:
                game.snake.change_direction(game.snake.dict_direction[constants.left])
            
    game.snake.move()
    
    