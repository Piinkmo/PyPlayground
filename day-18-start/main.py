import random
import turtle
from ast import copy_location
from turtle import Screen

import heroes
import villains
import turtle as t

tim = t.Turtle()
t.colormode(255)

t.speed(0) # control the speed of drawing

# def random_color():
#     r = random.randint(0,255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     random_color = (r,g,b)
#     return random_color

# List of colors to cycle through for each shape
colors = ["red", "blue", "green", "pink", "orange", "wheat", "SeaGreen", "SlateGray", "DeepSkyBlue"]
directions = [0, 90, 180, 270]
tim.pensize(10)

# def dashed_line(length, dashed_length):
#     for _ in range(length // (2 * dashed_length)):
#         tim.forward(10)
#         tim.penup()
#         tim.forward(10)
#         tim.pendown()
#
# dashed_line(100, 10)

# def polygon(sides, length, color):
#     t.color(color)
#     angle = 360 / sides
#     for _ in range(sides):
#         t.forward(length)
#         t.left(angle)
#
# def reset_position():
#     t.penup()
#     t.goto(0,0)
#     t.pendown()
#
# side_length = 50
# for i, sides in enumerate(range(4, 9)):
#     reset_position()
#     color = colors[i % len(colors)]
#     polygon(sides, side_length, color)

# for _ in range(200):
#     tim.color(random.choice(colors))
#     tim.forward(30)
#     tim.setheading(random.choice(directions))

# Set the pen color for drawing
turtle.colormode(255)  # Allows us to use RGB colors
def draw_spirograph(size_of_gap, radius):
    for i in range(int(360 / size_of_gap)):
        r = (i * 10) % 255  
        g = (i * 20) % 255  
        b = (i * 30) % 255  
        t.pencolor(r, g, b)  
        t.circle(radius)     
        t.left(size_of_gap)  


draw_spirograph(10, 100)
# Finish the drawing
turtle.done()

screen = t.Screen()
screen.exitonclick()
