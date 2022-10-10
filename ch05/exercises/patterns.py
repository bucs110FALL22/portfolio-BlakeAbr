#Function that creates normal pyramid
def star_pyramid():
  rows = int(input("Please enter the number of rows for a pyramid: "))
  for i in range(rows):
    for j in range(i+1):
        print("*", end="")
    print("\n")
    
star_pyramid()
#Function that creates reverse pyramid
def rstar_pyramid():
  rows = int(input("Please enter the number of rows for a reverse pyramid: "))
  for i in range(rows, 0, -1):
    for j in range(0, i):
        print("*", end="")
    
    print("\n")

rstar_pyramid()