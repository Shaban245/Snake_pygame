import resourse
import pygame
from src import constants
from random import randint as rd

class Chery:
    def __init__(self):
        self.image = pygame.image.load("resourse/Chery.jpg")
        self._allowed_x = constants.allowed_chery_x
        self._allowed_y = constants.allowed_chery_y
        self.x_cor = rd(0, self._allowed_x)
        self.y_cor = rd(0, self._allowed_y)
        
        
    def generate_new_position(self) -> None:
        self.x_cor = rd(0, self._allowed_x)
        self.y_cor = rd(0, self._allowed_y)
        