class Rectangle:

  def __init__ (self, x, y, height, width):
    #passes the arguments through init and creates them
    #args
    #self - the object itself
    #x - the x value of the rectangle
    #y - the y value of the rectangle
    #height - the height of the rectangle
    #width - the width of the rectangle
  
    self.x = x
    self.y = y
    self.height = height
    self.width = width
    if self.x < 0:
      self.x = 0
    if self.y < 0:
      self.y = 0
    if self.width < 0:
      self.width = 0
    if self.height < 0:
      self.height = 0

  def __str__(self):
    #creates a string showing x,y,h,w
    #args: self - an instance of an object
    #return: (str) returns all the dimensions of the rectangle in the form of a string
    return str("x: ",self.x, "y: ", self.y,"height: ",self.height, "width: ",self.width)