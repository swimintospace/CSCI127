#Name: Eliyas Philip
#Email: eliyas.philip84@myhunter.cuny.edu
#Date: October 10, 2021 
#This program displays a square eye


import turtle 
turtle.colormode(255)
wn = turtle.Screen()
stepa = turtle.Turtle()

stepa.speed(0)
stepa.pensize(5)
wn.bgcolor("khaki")

for i in range (36):
    stepa.pencolor(0, i * 7, 0)
    stepa.forward(10)
    stepa.left(10)

    for i in range (4):
        stepa.left(90)
        stepa.forward(300)
        stepa.backward(50)

wn.exitonclick()