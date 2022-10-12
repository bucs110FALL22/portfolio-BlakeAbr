#Exercise for 10/12
import turtle

turtle = turtle.Turtle()
turtle.color('green')
num_sides = int(input("How many sides do you want the shape to have? "))
side_length = int(input("How long do you want each side to be? "))

def drawEqShape(turtle, num_sides, side_length):
    for i in range(num_sides):
        turtle.forward(side_length)
        turtle.right(360/num_sides)

drawEqShape(turtle, num_sides, side_length)