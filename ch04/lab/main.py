import pygame
pygame.init()
import random
import math
##Selection Screen
for i in range(1):
  print("Please click your mouse to decide who you want to win Purple(Left) or Green(Right) ")
UP = 0
GUESS = 0
while UP == 0:
  for event in pygame.event.get():  # For Loop
        if event.type == pygame.QUIT:
            exit_game = True
        elif event.type == pygame.MOUSEBUTTONDOWN:  # Click event
            if event.button == 3:
                print("User clicked RIGHT mouse button, guessed Green to Win. ")
                UP = UP + 1
                GUESS = GUESS + 1
            if event.button == 1:
              print("User clicked LEFT mouse button, guessed Purple to Win.")
              UP = UP + 1
              GUESS = GUESS + 2
  green =(127,255,0)
  purple = (178,58,238)
  screenheight = 300
  screenwidth = 300
  size = (screenwidth, screenheight)
  window = pygame.display.set_mode(size)
  window.fill(green)
  rect = pygame.draw.rect(window, purple, pygame.Rect(0, 0, 150, 300))
  pygame.display.flip()

  

  
# Creating a game loop

import pygame
pygame.init()
  
# Creating window


pygame.time.wait(1000)

##Dartboard
pink = (233,150,122)
blue = (0, 0, 255)
black = (0,0,0)
pygame.init()
screenheight = 300
screenwidth = 300
size = (screenwidth, screenheight)
window = pygame.display.set_mode(size)
window.fill(blue)
pygame.draw.circle(window, pink, ((150,150)), 150 )
pygame.draw.line(window, black, ((150,300)), ((150,0)))
pygame.draw.line(window, black, ((0,150)), ((300,150)))
pygame.display.flip()
##part b



yellow = (255,255,0)
playergreen = 0
playerpurple = 0
for i in range(20):
  pygame.time.wait(1000)
  pygame.draw.circle(window, pink, ((150,150)), 150 )
  pygame.draw.line(window, black, ((150,300)), ((150,0)))
  pygame.draw.line(window, black, ((0,150)), ((300,150)))
  pygame.display.flip()
  xvalue = (random.randrange(0,screenwidth))
  yvalue = (random.randrange(0,screenheight))
  distance_from_center = math.hypot(xvalue, yvalue) #the distance formula
  is_in_circle = distance_from_center <= screenwidth/2
  if is_in_circle == True and i % 2 == 0:
    print("Hit")
    playerpurple = playerpurple + 1
    pygame.draw.circle(window, yellow, ((150,150)), 150 )
    pygame.draw.line(window, black, ((150,300)), ((150,0)))
    pygame.draw.line(window, black, ((0,150)), ((300,150)))
    pygame.display.flip()
  elif is_in_circle == True and i % 2 != 0:
    print("Hit")
    pygame.draw.circle(window, yellow, ((150,150)), 150 )
    pygame.draw.line(window, black, ((150,300)), ((150,0)))
    pygame.draw.line(window, black, ((0,150)), ((300,150)))
    pygame.display.flip()
    playergreen = playergreen + 1
  else:
    print("Miss")
  


print("Green Player's score " + str(playergreen))
print("Purple Player's score " + str(playerpurple))

if playergreen > playerpurple:
  print("Green won!")
else:
  print("Purple won!")

if GUESS == 1 and playergreen > playerpurple:
  print("You Guessed Right!")
elif GUESS == 2 and playergreen < playerpurple:
  print("You Guessed Right!")
elif GUESS == 1 and playergreen < playerpurple:
  print("You Guessed Wrong :C")
elif GUESS == 2 and playergreen > playerpurple:
  print("You Guessed Wrong :C")
else:
  print("They tied.")


  
