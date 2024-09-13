#--------------------------------------------------------------------------
# import colorgram
# import random

# Code pulls rgb values from downloaded Hirst image and creates a color_list
# rgb_list = []
# color_list = colorgram.extract("image.jpg",30)
#
# for colors in color_list:
#     # art_color = color_list[random.randint(0, 29)]
#     r = colors.rgb[0]
#     g = colors.rgb[1]
#     b = colors.rgb[2]
#     new_color = (r, g, b)
#     rgb_list.append(new_color)
# print(rgb_list)
#--------------------------------------------------------------------------
import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)

tim = Turtle()
tim.speed("fastest")
tim.hideturtle()


def paint_x():
    """Moves the turtle object in an XY pattern randomizing the dot color for every position."""
    x_value = -250
    for _ in range(10):
        tim.teleport(x_value, y_value)
        tim.color(color_list[random.randint(0, 28)])
        tim.dot(20)
        x_value += 50


color_list = [(227, 234, 242), (245, 234, 239), (233, 242, 236), (208, 158, 96), (234, 213, 101), (41, 104, 144),
              (149, 78, 57), (130, 168, 194), (202, 137, 162), (148, 65, 83), (24, 40, 55), (204, 90, 68),
              (169, 159, 55), (139, 180, 152), (193, 89, 121), (59, 117, 93), (26, 44, 36), (223, 171, 187),
              (63, 46, 34), (91, 154, 104), (44, 161, 182), (237, 212, 7), (226, 175, 167), (13, 96, 75), (41, 59, 99),
              (179, 189, 213), (99, 125, 168), (65, 33, 43), (104, 43, 59)]

y_value = -250
for _ in range(10):
    paint_x()
    y_value += 50

screen = Screen()
screen.exitonclick()
