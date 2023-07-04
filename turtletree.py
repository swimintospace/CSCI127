#Name: Eliyas Philip
#Email: eliyas.philip84@myhunter.cuny.edu
import turtle

def setUp():
    t = turtle.Turtle()
    t.hideturtle()
    t.setheading(90)
    t.speed(speed=0)
    return t

def fractalRight(t, distance, i):
    if distance > 10:
        i == i%255
        t.color(0,i,0)
        t.right(30)
        t.forward(distance)
        t.stamp()
        newDistance = distance - 5
        fractalRight(t,newDistance,i+25)
        t.backward(distance)
        t.left(30)
        fractalLeft(t,newDistance,i+25)

def fractalLeft(t, distance,i):
    if distance > 10:
        i == i%255
        t.color(0,i,0)
        t.left(30)
        t.forward(distance)
        t.stamp()
        newDistance = distance - 5
        fractalLeft(t,newDistance,i+25)
        t.backward(distance)
        t.right(30)
        fractalRight(t,newDistance,i+25)

def main():
    t = setUp()
    turtle.colormode(255)
    turtle.bgcolor("khaki")
    t.forward(50)
    fractalRight(t,50,0)
    fractalLeft(t,50,0)

if __name__ == "__main__":
    main()