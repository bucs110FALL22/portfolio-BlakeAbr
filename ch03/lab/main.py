#1. import modules
import turtle
import random
# modules for part B
import pygame
import math

#Part A

# 2.  Create a screen
window = turtle.Screen() 
window.bgcolor('lightblue')

# 3.  Create two turtles
michelangelo = turtle.Turtle() 
leonardo = turtle.Turtle()
michelangelo.color('orange')
leonardo.color('blue')
michelangelo.shape('turtle')
leonardo.shape('turtle')

# 4. Pick up the pen so we don’t get lines
michelangelo.up() 
leonardo.up()
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

## 5. Your PART A code goes here
for move in range(10):
  michelangelo.down()
  leonardo.down()
  michelangelo.forward(random.randrange(1,11))
  leonardo.forward(random.randrange(1,11))
michelangelo.up()
leonardo.up()
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)




# PART B - complete part B here



red = (255, 0, 0)
green = (0, 255, 0)
pygame.init()
size = (400, 400)
window = pygame.display.set_mode(size)
pygame.time.wait(1000)
window.fill(green)



#PRINTS THE EQUILATERAL TRIANGLE
coords = []
num_sides = 3
side_length = 50
offset = 200

for i in range(num_sides):
    theta = ((2.0 * math.pi * (i)) / num_sides)
    x = side_length * math.cos(theta) + offset
    y = side_length * math.sin(theta) + offset
    coords.append((x,y))
    print(coords)
pygame.time.wait(1000)
pygame.display.flip()
pygame.draw.polygon(window, red, coords)
pygame.time.wait(1000)
pygame.display.flip()
pygame.time.wait(1000)
window.fill(green)
pygame.display.flip()

#PRINTS THE SQUARE
coords = []
num_sides = 4
side_length = 50
offset = 200

for i in range(num_sides):
    theta = ((2.0 * math.pi * (i)) / num_sides)
    x = side_length * math.cos(theta) + offset
    y = side_length * math.sin(theta) + offset
    coords.append((x,y))
    print(coords)
pygame.time.wait(1000)
pygame.display.flip()
pygame.draw.polygon(window, red, coords)
pygame.time.wait(1000)
pygame.display.flip()
pygame.time.wait(1000)
window.fill(green)
pygame.display.flip()

#PRINTS THE HEXAGON
coords = []
num_sides = 6
side_length = 50
offset = 200

for i in range(num_sides):
    theta = ((2.0 * math.pi * (i)) / num_sides)
    x = side_length * math.cos(theta) + offset
    y = side_length * math.sin(theta) + offset
    coords.append((x,y))
    print(coords)
pygame.time.wait(1000)
pygame.display.flip()
pygame.draw.polygon(window, red, coords)
pygame.time.wait(1000)
pygame.display.flip()
pygame.time.wait(1000)
window.fill(green)
pygame.display.flip()

## PRINTS THE NONAGON
coords = []
num_sides = 9
side_length = 50
offset = 200

for i in range(num_sides):
    theta = ((2.0 * math.pi * (i)) / num_sides)
    x = side_length * math.cos(theta) + offset
    y = side_length * math.sin(theta) + offset
    coords.append((x,y))
    print(coords)
pygame.time.wait(1000)
pygame.display.flip()
pygame.draw.polygon(window, red, coords)
pygame.time.wait(1000)
pygame.display.flip()
pygame.time.wait(1000)
window.fill(green)
pygame.display.flip()


## PRINTS THE CIRCLE
coords = []
num_sides = 360
side_length = 50
offset = 200

for i in range(num_sides):
    theta = ((2.0 * math.pi * (i)) / num_sides)
    x = side_length * math.cos(theta) + offset
    y = side_length * math.sin(theta) + offset
    coords.append((x,y))
    
pygame.time.wait(1000)
pygame.display.flip()
pygame.draw.polygon(window, red, coords)
pygame.time.wait(1000)
pygame.display.flip()
pygame.time.wait(1000)
window.fill(green)
pygame.display.flip()

  
  