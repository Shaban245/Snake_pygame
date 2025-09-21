from src.Field import Field
from src.Snake import Snake


class Game:
    
    def __init__(self):
        self.snake = Snake()
        self.field = Field()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.field.width, self.field.heigth))