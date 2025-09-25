import pygame
from src.field import Field
from src.Snake import Snake
from src.chery import Chery
from src import constants
from src.score import Score
from src.tail import Tail


class Game:
    
    def __init__(self):
        self.snake = Snake()
        self.field = Field()
        self.chery = Chery()
        self.score = Score()
        self.tails = []
        self.clock = pygame.time.Clock()
        self.fps = constants.FPS
        self.screen = pygame.display.set_mode((self.field.width, self.field.heigth))
    
    def update_screen(self) -> None:
        pygame.display.update()
        self.screen.fill(self.field.rgb_color)
        self.blit_chery()
        self.blit_snake()
        self.clock_tick()
        self.blit_score()
        self.snake.move()
        self.out_of_Field()

        
    def blit_snake(self) -> None:
        self.screen.blit(self.snake.image, (self.snake.x_position, self.snake.y_position))
        
    def clock_tick(self) -> None:
        self.clock.tick(self.fps)
    
    def blit_chery(self) -> None:
        self.screen.blit(self.chery.image, (self.chery.x_cor, self.chery.y_cor))
        
    def blit_score(self) -> None:
        self.screen.blit(self.score.text, (self.score.x_cor, self.score.y_cor))
        
    def eat_chery(self) -> None:
        if self.snake.rect_snake.colliderect(self.chery.rect_chery):
            self.chery.generate_new_position()
            self.score.update_score()
            
            
    def out_of_Field(self):
        if self.snake.x_position > constants.rigth_limits_field or self.snake.x_position < constants.left_limits_field:
            exit()
        elif self.snake.y_position > constants.down_lomits_field or self.snake.y_position < constants.upper_limits_field:
            exit()
        

        
    
        