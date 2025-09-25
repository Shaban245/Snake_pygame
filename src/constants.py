
WIDTH_field =  1000
HEIGHT_field = 700
rgb_color_field = (51, 255 , 51)
FPS = 30
SNAKE_speed = 5

x_cor_snake = WIDTH_field /2
y_cor_snake = HEIGHT_field / 2
x_speed = 5
y_speed = 0
dict_direction = {"rigth": (SNAKE_speed, 0),
                  "left": (-SNAKE_speed, 0),
                  "up": (0, -SNAKE_speed),
                  "down": (0, SNAKE_speed)}
rigth = "rigth"
left = 'left'
up = 'up'
down = 'down'

allowed_chery_x = WIDTH_field - 50
allowed_chery_y = HEIGHT_field - 50
min_chery_x = 100
min_chery_y = 100

rect_width_snake = 20
rect_heigth_snake = 20

rect_width_chery = 20
rect_heigth_chery = 20

score_x_cor = 50
score_y_cor = 50
size_font = 50

upper_limits_field = -10
left_limits_field = -10
down_lomits_field = HEIGHT_field -10
rigth_limits_field = WIDTH_field -10