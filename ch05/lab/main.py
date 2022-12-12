import pygame
pygame.init()

#Part A / B

def threenplus1():
  count = 0
  upperlimit = 20
  iters = {}
  start = 2
  max_so_far = 0

  display = pygame.display.set_mode()
  n = int(input("Please choose a positive number: "))
  print(n)
  for i in range(start, upperlimit):
    while n > 1:
      count = count + 1
      if n % 2 == 0:
          n = n / 2
          print(n)
      else:
        n = (3*n) + 1
        print(n)
      if count > max_so_far:
            max_so_far = count
      iters[n] = count
      coords = []
    
    
    
  print("There were " + str(count) +" iterations")
  iters[i] = count
  print(iters)

threenplus1()
  
