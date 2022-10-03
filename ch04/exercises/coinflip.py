import turtle
import random

turtle.screensize(canvwidth=200, canvheight=200,bg="green")
turtle69 = turtle.Turtle()
turtle69.shape("turtle")
turtle69.color('purple')
turtle69.setpos(0,0)
canvwidth = turtle.window_width()
canvheight = turtle.window_height()


while abs(turtle69.xcor()) < (canvwidth/2) and (turtle69.ycor()) < (canvheight/2):
  mylist = ["heads", "tails"]
  coinflip = random.choice(mylist)
  print(random.choice(mylist))
  if coinflip == "heads":
    turtle69.left(90)
    turtle69.forward(50)
  elif coinflip == "tails":
    turtle69.right(90)
    turtle69.forward(50)

  

  