import pygame
from src import constants


class Tail:
    
    def __init__(self):
        self.x_cor = 0
        self.y_cor = 0
        self.tail_rect = pygame.Rect(self.x_cor, self.y_cor, constants.rect_width_snake, constants.rect_heigth_snake)
        self.tail_draw = pygame.draw(x_cor, y_cor)
        