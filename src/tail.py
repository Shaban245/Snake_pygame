import pygame
from src import constants


class Tail:
    
    def __init__(self, x_cor, y_cor) -> None:
        self.x_cor = x_cor
        self.y_cor = y_cor
        self.tail_rect = pygame.Rect(self.x_cor, self.y_cor, constants.rect_width_snake, constants.rect_heigth_snake)
        self.color = "Red"

    
    def draw_tail(self, screen) -> None:
        pygame.draw.circle(screen, self.color, (self.x_cor, self.y_cor), 10)
        