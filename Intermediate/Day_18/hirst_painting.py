import random
from turtle import Turtle, Screen, colormode

color_list = [(206, 161, 82), (55, 88, 129), (142, 91, 41), (221, 207, 107), (138, 26, 48), (133, 175, 200),
              (157, 47, 84), (46, 55, 102), (169, 159, 41), (131, 188, 145), (82, 20, 43), (36, 43, 68), (186, 93, 106),
              (189, 139, 163), (87, 115, 177), (87, 156, 97), (59, 39, 33), (79, 154, 165), (196, 81, 71),
              (54, 128, 122), (45, 73, 76), (162, 202, 216), (44, 75, 73), (78, 76, 45), (167, 207, 165),
              (219, 175, 187), (218, 182, 169), (180, 188, 211), (142, 37, 33), (40, 63, 61)]

print(random.choice(color_list))

colormode(255)
tim = Turtle()
tim.speed("fastest")

tim.penup()
start_x = -250
start_y = -250

tim.setposition(start_x, start_y)
for i in range(10):
    tim.setposition(start_x, start_y + (i * 50))
    for _ in range(10):
        tim.forward(50)
        tim.dot(20, random.choice(color_list))

screen = Screen()
screen.exitonclick()
