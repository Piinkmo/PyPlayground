import colorgram
from PIL.ImImagePlugin import number
from PIL.ImageChops import screen

rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

print(rgb_colors)

import turtle as turtle_module
import random

turtle_module.speed("fastest")

turtle_module.colormode(255)
tim = turtle_module.Turtle()
color_list = [(251, 249, 245), (210, 165, 122), (246, 232, 234), (140, 49, 106), (164, 169, 38), (245, 79, 56), (218, 234, 231), (232, 112, 163), (3, 141, 50), (64, 200, 221), (1, 143, 185), (241, 65, 139), (162, 55, 52), (19, 165, 126), (254, 230, 0), (209, 219, 223), (237, 218, 76), (29, 197, 219), (143, 181, 159), (217, 176, 191), (247, 168, 148), (144, 213, 224), (190, 190, 193), (163, 211, 184), (103, 46, 96), (2, 121, 33), (144, 42, 38)]

tim.setheading(225)
tim.forward(250)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)





screen = random.choice(color_list)





