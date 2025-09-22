import pygame
from src.Game import Game
from src import constants

pygame.init()

game = Game()





while True:

    game.update_screen(game)
    game.blit_snake(game)
    game.blit_chery(game)
    game.eat_chery(game)
    game.clock_tick(game)
    

    
    
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
    
    