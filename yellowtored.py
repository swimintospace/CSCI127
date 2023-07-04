#Name: Eliyas Philip
#Email: eliyas.philip84@myhunter.cuny.edu
#Date: September 28, 2021
#A program that changes turtle shade from yellow to red

import turtle 
turtle.colormode(255)
keem = turtle.Turtle()
wn = turtle.Screen()
keem.shape("turtle")

keem.right(90)

for i in range (0, 255, 10):
    keem.forward(10)
    keem.pensize(i)
    keem.color(255,255-i,0)

keem.penup()
keem.pensize(0)
keem.color(0, 0, 0)
keem.backward(260)


keem.left(90)
keem.pendown()

for i in range(0, 255, 10):
    keem.forward(10)
    keem.pensize(i)
    keem.color(255, 255-i, 0)

wn.exitonclick()