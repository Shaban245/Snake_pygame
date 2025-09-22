from src.field import Field
from src.Snake import Snake
import pygame
from src.constants import FPS


class Game:
    
    def __init__(self):
        self.snake = Snake()
        self.field = Field()
        self.clock = pygame.time.Clock()
        self.fps = FPS
        self.screen = pygame.display.set_mode((self.field.width, self.field.heigth))
    
    def update_screen(self, game) -> None:
        pygame.display.update()
        game.screen.fill(game.field.rgb_color)
        
    def blit_snake(self, game) -> None:
        game.screen.blit(game.snake.image, (game.snake.x_position, game.snake.y_position))
        
    def clock_tick(self, game) -> None:
        game.clock.tick(self.fps)