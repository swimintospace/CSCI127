#Name: Eliyas Philip
#Email: eliyas.philip84@myhunter.cuny.edu
#Date: October 3, 2021 
#This program makes a spiral using a turtle stamps which are based on user input, 

stamps = input("Enter number of stamps: ")
stamps = int(stamps)

import turtle
wn = turtle.Screen()
turtle.colormode(255)
ken = turtle.Turtle()
ken.shape('circle')
ken.penup()


steps = 10
red = 186
green = 164 
blue = 145 

ken.color(red, green, blue)

for i in range(stamps):
    ken.stamp()
    steps += 2
    
    if red + 3 <= 255 and green + 3 <= 255 and blue + 3 <= 255:
        red, green, blue = red + 3, green + 3, blue + 3 
    
    ken.color(red, green, blue)
    ken.forward(steps)
    ken.right(24)

wn.exitonclick()