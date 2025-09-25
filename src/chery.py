import resourse
import pygame
from src import constants
from random import randint as rd

class Chery:
    def __init__(self):
        self.image = pygame.image.load("resourse/Chery.jpg")
        self._allowed_x = constants.allowed_chery_x
        self._allowed_y = constants.allowed_chery_y
        self.min_x_chery = constants.min_chery_x
        self.mim_y_chery = constants.min_chery_y
        self.x_cor = self.generate_new_x()
        self.y_cor = self.generate_new_y()
        self.rect_chery = pygame.Rect(self.x_cor, self.y_cor, constants.rect_width_chery, constants.rect_heigth_chery)
        
        
        
    def generate_new_position(self) -> None:
        self.x_cor = self.generate_new_x()
        self.y_cor = self.generate_new_y()
        self.rect_chery = pygame.Rect(self.x_cor, self.y_cor, constants.rect_width_chery, constants.rect_heigth_chery)
        
        
    def generate_new_x(self) -> int:
        return rd(self.min_x_chery, self._allowed_x)
    
    def generate_new_y(self) -> int:
        return rd(self.mim_y_chery, self._allowed_y)
        