#Name: Eliyas Philip
#Email: eliyas.philip84@myhunter.cuny.edu
#Date: September 29, 2021
#A program that takes user input to decide the turtle color and draws a square

import turtle 
wn = turtle.Screen()
nick = turtle.Turtle()


hex = input("Please enter a 6-digit Hexadecimal number: ")
hex = "#" + hex
nick.color(hex)
nick.shape('turtle')

for i in range(4):
    nick.left(90)
    nick.forward(100)
    nick.stamp()


wn.exitonclick()