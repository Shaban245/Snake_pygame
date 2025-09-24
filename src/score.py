import pygame 
import resourse
from src import constants


class Score:
    
    def __init__(self):
        self.font = pygame.font.Font('resourse/RishaNeo.ttf', constants.size_font)
        self.score = 0
        self.text = self.font.render(f'Score: {self.score}', True, 'White')
        self.x_cor = constants.score_x_cor
        self.y_cor = constants.score_y_cor
        
    
    def update_score(self) -> None:
        self.score += 1
        self.text = self.font.render(f'Score: {self.score}', True, 'White')
