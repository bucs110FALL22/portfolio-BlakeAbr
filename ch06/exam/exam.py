import turtle

angle = 90
turns = 2
myturtle = turtle.Turtle()
myturtle.speed("fastest")

def screenmaker(color, name):
  #Creates the screen, and returns it
  #args 
  #(str)color : color of the screen
  #(str)name : name on top the screen
  #return : the screen
    screen = turtle.Screen()
    screen.bgcolor(color)
    screen.title(name)
    return screen
def wallsmall(x=0, y=0, width=0, height=0, color=None):
  #Creates the main gray wall in the middle
  #args
  #(int) x: the x value the turtle will go to
  #(int) y: the y value the turtle will go to
  #(int) width: the width of the shape, the value the turtle will go
  #(int) height: the height of the shape, turtle moves this amount
  #(str) color: the color the wall will be
    myturtle.penup()
    myturtle.goto(x,y)
    myturtle.pendown()
    for i in range(turns):
        myturtle.fillcolor(color)
        myturtle.color(color)
        myturtle.begin_fill()
        myturtle.forward(width)
        myturtle.left(angle)
        myturtle.forward(height)
        myturtle.left(angle)
        myturtle.end_fill()
def thickwalls(x=0, y=0, width=0, height=0, color=None):
  #Creates the two slightly taller walls on the sides
  #(int) x: the x value the turtle will go to
  #(int) y: the y value the turtle will go to
  #(int) width: the width of the shape, the value the turtle will go
  #(int) height: the height of the shape, turtle moves this amount
  #(str) color: the color the wall will be
    myturtle.penup()
    myturtle.goto(x,y)
    myturtle.pendown()
    for i in range(turns):
        myturtle.fillcolor(color)
        myturtle.color(color)
        myturtle.begin_fill()
        myturtle.forward(width)
        myturtle.left(angle)
        myturtle.forward(height)
        myturtle.left(angle)
        myturtle.end_fill()
    myturtle.goto(x+300, y)
    for i in range(turns):
        myturtle.fillcolor(color)
        myturtle.color(color)
        myturtle.begin_fill()
        myturtle.forward(width)
        myturtle.left(angle)
        myturtle.forward(height)
        myturtle.left(angle)
        myturtle.end_fill()
def bricks(x=0,y=0,width=0):
  #Draws three lines through the middle wall to add more detail
  #(int) x: the x value the turtle will go to
  #(int) y: the y value the turtle will go to
  #(int) width: the width of the shape, the value the turtle will go
    myturtle.pensize(2)
    myturtle.pu()
    myturtle.goto(x,y)
    myturtle.pd()
    myturtle.forward(width)
    myturtle.pu()
    myturtle.goto(x,y+50)
    myturtle.pd()
    myturtle.forward(width)
    myturtle.pu()
    myturtle.goto(x,y+100)
    myturtle.pd()
    myturtle.forward(width)
def fingers(x=0,y=0,radius=0,color=None):
  #Draws the fingers grabbing the wall
  #(int) x: the x value the turtle will go to
  #(int) y: the y value the turtle will go to
  #(int) radius: the radius of the circle the turtle will make
  #(str) color: the color the circle will be
    spacebetweendigits = 15
    myturtle.pensize(1)
    myturtle.pu()
    myturtle.goto(x,y)
    def drawfingers():
      #Function to draw each individual digit.
            myturtle.pd()
            myturtle.fillcolor(color)
            myturtle.color(color)
            myturtle.begin_fill()
            myturtle.circle(radius)
            myturtle.end_fill()
    drawfingers()
    myturtle.pu()
    myturtle.backward(spacebetweendigits)
    drawfingers()
    myturtle.pu()
    myturtle.backward(spacebetweendigits)
    drawfingers()
    myturtle.pu()
    myturtle.backward(spacebetweendigits)
    drawfingers()

def colossalhead(x=0,y=0,radius=0,color=None):
  #Draws the red part of the head
  #Draws the fingers grabbing the wall
  #(int) x: the x value the turtle will go to
  #(int) y: the y value the turtle will go to
  #(int) radius: the radius of the circle the turtle will make
  #(str) color: the color the circle will be
    myturtle.pu()
    myturtle.goto(x,y)
    myturtle.pd()
    myturtle.fillcolor(color)
    myturtle.color(color)
    myturtle.begin_fill()
    myturtle.circle(radius)
    myturtle.end_fill()
def forehead(x=0,y=0,color=None,radius=0):
  #Draws the forehead of the Titan
  #(int) x: the x value the turtle will go to
  #(int) y: the y value the turtle will go to
  #(int) radius: the radius of the circle the turtle will make
  #(str) color: the color the circle will be
    myturtle.pu()
    myturtle.goto(x,y)
    myturtle.pd()
    myturtle.fillcolor(color)
    myturtle.color(color)
    myturtle.begin_fill()
    myturtle.right(angle)
    myturtle.circle(radius,-180)
    myturtle.end_fill()
def teeth(x=0,y=0,color1=None,width=0):
  #Creates a straight white line to resemble where the teeth would be
  #(int) x: the x value the turtle will go to
  #(int) y: the y value the turtle will go to
  #(int) width: the width of the line the turtle will make
  #(str) color1: the color the line will be
    myturtle.pensize(10)
    myturtle.pu()
    myturtle.goto(x,y)
    myturtle.pd()
    myturtle.right(angle)
    myturtle.fillcolor(color1)
    myturtle.color(color1)
    myturtle.begin_fill()
    myturtle.forward(width)
    myturtle.end_fill()
def cheekmuscles(x=0,y=0,color=None,width=0):
  #Creates two diagonal peach lines to symbolize the cheek muscles
  #(int) x: the x value the turtle will go to
  #(int) y: the y value the turtle will go to
  #(int) width: the width of the line the turtle will make
  #(str) color: the color the line will be
    myturtle.left(angle)
    myturtle.pensize(5)
    myturtle.pu()
    myturtle.goto(x,y)
    myturtle.pd()
    myturtle.color(color)
    myturtle.right(angle+30)
    myturtle.forward(width)
    myturtle.pu()
    myturtle.goto(x+140,y)
    myturtle.pd()
    myturtle.right(angle+30)
    myturtle.forward(width)
def nose(x=0,y=0,width=0,angle=0):
  #Creates a wheat line in the middle to represent the nose
  #(int) x: the x value the turtle will go to
  #(int) y: the y value the turtle will go to
  #(int) width: the width of the line the turtle will make
  #(int) angle: the angle that the turtle will turn
    myturtle.pensize(9)
    myturtle.right(angle)
    myturtle.pu()
    myturtle.goto(x,y)
    myturtle.pd()
    myturtle.forward(width)
def eyes(x=0,y=0,radius=0,color=None):
  #Creates two black circles for the eyes
  #(int) x: the x value the turtle will go to
  #(int) y: the y value the turtle will go to
  #(int) radius: the radius of the circle the turtle will make
  #(str) color: the color the circle will be
    myturtle.pu()
    myturtle.goto(x,y)
    myturtle.pd()
    myturtle.color(color)
    myturtle.begin_fill()
    myturtle.circle(radius)
    myturtle.pu()
    myturtle.goto(x+60,y)
    myturtle.circle(radius+3.5)
    myturtle.end_fill()
    myturtle.pd()
def pupils(x=0,y=0,radius=0,color=None):
  #Inserts two yellow dots as pupils into the eyes
  #(int) x: the x value the turtle will go to
  #(int) y: the y value the turtle will go to
  #(int) radius: the radius of the circle the turtle will make
  #(str) color: the color the circle will be
    myturtle.pu()
    myturtle.goto(x,y)
    myturtle.pd()
    myturtle.dot(radius,color)
    myturtle.pu()
    myturtle.goto(x+57,y)
    myturtle.dot(radius,color)
#Driving code
def main():
    screenmaker("lightblue","The Colossal Titan's First Appearance!!")
    wallsmall(-200,-125,350,175,"gray")
    thickwalls(-200,-125,50, 200, "lightgray")
    bricks(-150, -75, 300)
    fingers(-90,40,10,"red")
    colossalhead(0,52,70, "red")
    forehead(-70,130,"wheat",70)
    teeth(-62,90,"white", 120)
    cheekmuscles(-70,130,"wheat",130)
    nose(-0,90,100,120)
    eyes(-20,130,10,"black")
    pupils(-30,130,5,"yellow")
    myturtle.hideturtle()
    turtle.exitonclick()
main()
