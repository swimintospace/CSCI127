#Name: Eliyas Philip
#Email: eliyas.philip84@myhunter.cuny.edu
#Date: September 27, 2021
#A program that demonstrates shades of yellow 

import turtle 

turtle.colormode(255)
jess = turtle.Turtle()
wn = turtle.Screen()
jess.shape("turtle")
jess.left(60)


for i in range (0,255,10):
    jess.forward(10)
    jess.pensize(i)
    jess.color(i, i, 0)


jess.penup()
jess.pensize(0)
jess.color(0, 0, 0)
jess.backward(260)


jess.left(60)
jess.pendown()


for i in range(0, 255, 10):
    jess.forward(10)
    jess.pensize(i)
    jess.color(i, i, 0)
wn.exitonclick()

