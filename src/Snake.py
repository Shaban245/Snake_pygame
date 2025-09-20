

class Snake:
    
    def __init__(self, x_cor, y_cor, x_speed, y_speed) -> None:
        self.x_cor = x_cor
        self.y_cor = y_cor
        self.x_speed = x_speed
        self.y_speed = y_speed
        
        
    def move(self) -> None:
        self.x_cor += self.x_speed
        self.y_cor += self.y_speed
        
        
    def change_direction(self, x: int, y: int) -> None:
        self.x_speed , self.y_speed = x, y
        
    