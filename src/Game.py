import pygame
from src.field import Field
from src.Snake import Snake
from src.chery import Chery
from src.constants import FPS


class Game:
    
    def __init__(self):
        self.snake = Snake()
        self.field = Field()
        self.chery = Chery()
        self.clock = pygame.time.Clock()
        self.fps = FPS
        self.screen = pygame.display.set_mode((self.field.width, self.field.heigth))
    
    def update_screen(self, game) -> None:
        pygame.display.update()
        game.screen.fill(game.field.rgb_color)
        self.blit_chery(game)
        self.blit_snake(game)
        self.clock_tick(game)
        
    def blit_snake(self, game) -> None:
        game.screen.blit(game.snake.image, (game.snake.x_position, game.snake.y_position))
        
    def clock_tick(self, game) -> None:
        game.clock.tick(self.fps)
    
    def blit_chery(self, game) -> None:
        game.screen.blit(game.chery.image, (game.chery.x_cor, game.chery.y_cor))
        
    def eat_chery(self, game) -> None:
        if self.snake.rect_snake.collidepoint(self.chery.rect_chery.center):
            game.chery.generate_new_position()
        