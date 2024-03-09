import turtle

import colorgram
from turtle import Turtle
from turtle import Screen
import random

tim = Turtle()
tim.hideturtle()
turtle.colormode(255)

colors = [(209, 165, 125), (249, 234, 237), (140, 48, 106),
 (164, 169, 38), (244, 80, 56), (3, 143, 55), (233, 109, 162), (215, 234, 232),
 (241, 65, 140), (1, 143, 184), (162, 55, 52), (57, 202, 224), (254, 230, 0),
 (20, 166, 126), (211, 232, 236), (244, 223, 50), (27, 197, 219), (162, 184, 171),
 (233, 165, 191), (191, 191, 193), (141, 213, 225), (243, 170, 153), (159, 212, 181),
 (106, 45, 98), (9, 115, 37), (131, 45, 38)]

tim.setx(0)
tim.sety(0)

def random_color():
    random_colors = random.choice(colors)
    return random_colors


def draw_circles():
    for _ in range(10):
        tim.color(random_color())
        tim.dot(20)
        tim.penup()
        tim.forward(50)

keep_drawing = True
y = 0
while keep_drawing:
    draw_circles()
    y = y + 40
    tim.teleport(0,y)
    if y == 400:
        keep_drawing = False

screen = Screen()
screen.exitonclick()


'''Code to extract colors from a picture'''
# colors = colorgram.extract('image.jpg',45)

# first_color = colors[0]

# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)
# print(rgb_colors)
