import src.constants
import resourse
import pygame

class Snake:
    
    def __init__(self) -> None:
        self.x_position = src.constants.x_cor_snake
        self.y_position = src.constants.y_cor_snake
        self.x_speed = 5
        self.y_speed = 0
        self.image = pygame.image.load('resourse/tarzan.jpg')
        self.dict_direction = src.constants.dict_direction
        
        
        
    def move(self) -> None:
        self.x_position += self.x_speed
        self.y_position += self.y_speed
        
        
    def change_direction(self, dict: dict) -> None:
        self.x_speed , self.y_speed = dict[0], dict[1]
        
    
        
        
    
        
    