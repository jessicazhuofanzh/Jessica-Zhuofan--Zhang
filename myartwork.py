

from turtle import *

bgcolor("black")
pensize(1)
speed(0)

for i in range(12):
    for colours in ["cyan", "pink", "blue", "purple", "green", "yellow", "white"]:
        color(colours)
        circle(100)
        left(5)

for i in range(12):
    for colours in ["cyan", "pink", "blue", "purple", "green", "yellow", "white"]:
        color(colours)
        circle(150)
        left(5)

for i in range(24):
    for colours in ["cyan", "pink", "blue", "purple", "green", "yellow", "white"]:
        color(colours)
        circle(200)
        left(5)

hideturtle()




