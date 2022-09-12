import turtle

sides = int(input("How many sides do you want the shape to have? "))
length = int(input("How long do you want each side to be? "))
color_of_turtle = input("What color would you like the turtle to be? ")
my_turtle = turtle.Turtle()
my_turtle.shape("turtle")
my_turtle.color(color_of_turtle)
angle = 360/sides

for i in [angle] * sides:
  my_turtle.forward(length)
  my_turtle.left(i)

turtle.exitonclick()


