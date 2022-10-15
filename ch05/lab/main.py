import pygame
max_so_far = 0
scale = 5


n = int(input("Please choose a positive integer: "))
upperLimit = 20
iters = {}
count = 0
start = 2
for i in range(start, upperLimit):
  while n != 1:
    if n % 2 == 0:
        n = n / 2
        count = count + 1
    else:
        n = (3 * n) + 1
        count = count + 1
    if max_so_far < count:
      max_so_far = count
    print(n)
    iters[i] = count
coords = []
green = (0,255,0)
screenheight = 300
screenwidth = 300
size = (screenwidth, screenheight)
print(str(max_so_far) + "is the max")
threenplus1_iters_dict = list(iters.items())
coords = [(x* scale, y * scale) for x, y in iters.items()]
print(str(threenplus1_iters_dict) + "iterations")
print("There were " + str(count) + " items in the sequence before stopping at 1")
window = pygame.display.set_mode(size)
window.fill(green)
lines = pygame.draw.lines(window, green, True, coords)
pygame.display.flip()
