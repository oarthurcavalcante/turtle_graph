import turtle
import colorgram
import random
from turtle import Turtle, Screen

from PIL.ImageChops import screen

tim = Turtle()
screen = Screen()

screen.colormode(255)

color_list = [
    (245, 241, 233), (227, 234, 242), (245, 234, 239), (233, 242, 236), (208, 158, 96), (234, 213, 101), (41, 104, 144), (149, 78, 57), (130, 168, 194), (202, 137, 162), (148, 65, 83), (24, 40, 55), (204, 90, 68), (169, 159, 55), (139, 180, 152), (193, 89, 121), (59, 117, 93), (26, 44, 36), (223, 171, 187), (63, 46, 34), (91, 154, 104), (44, 161, 182), (237, 212, 7), (226, 175, 167), (13, 96, 75), (41, 59, 99), (179, 189, 213), (99, 125, 168), (65, 33, 43), (104, 43, 59)
]

tim.hideturtle()

tim.setheading(225)
tim.penup()
tim.forward(300)
tim.setheading(0)

for i in range(10):
    tim_x = tim.xcor()
    tim_y = tim.ycor()

    for _ in range(10):
        used_color = random.choice(color_list)
        tim.dot(20 , used_color)
        tim.penup()
        tim.forward(50)

    tim.goto(tim_x , tim_y + 50)





turtle.exitonclick()