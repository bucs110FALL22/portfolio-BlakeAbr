import Rectangle

class Surface:
  def __init__(self, filename, x, y, height, width):
    #passes the arguments through init and creates them
    #args
    #filename : used for the self image variable
    #self - the object itself
    #x - the x value of the rectangle
    #y - the y value of the rectangle
    #height - the height of the rectangle
    #width - the width of the rectangle
    self.rect = Rectangle.Rectangle(x,y,height,width)
    self.image = str(filename)
  def getRect(self):
    #self - the object that is being put through the function
    #returns the rectangle
    return(self.rect)
  