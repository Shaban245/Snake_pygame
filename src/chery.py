import images
import pygame
from src import constants
from random import randint as rd

class Chery:
    def __init__(self):
        self.image = pygame.image.load("images/Chery.jpg")
        self._allowed_x = constants.allowed_chery_x
        self._allowed_y = constants.allowed_chery_y
        
        
    def generate_new_position(self) -> list:
        ...