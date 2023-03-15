class Rectangle:
  
  def __init__(self,width,height):
    self.width = width
    self.height = height

  def __str__(self):
    return f"Rectangle(width={self.width}, height={self.height})"
  def set_width(self,width):
    self.width = width
    
  def set_height(self,height):
    self.height = height
    
  def get_area(self): 
    return self.width * self.height
    
  def get_perimeter(self): 
    return ((2*self.width)+(2*self.height))
  
  def get_diagonal(self): 
    return (((self.width**2)+(self.height**2))**0.5)

  def get_picture(self):
    if self.width>50 or self.height>50:
      return "Too big for picture."
    picture = ""
    for i in range(self.height):
      for j in range(self.width):
        picture+="*"
      picture+='\n'
    return picture
  
  def get_amount_inside(self,shape):
    self.shape = shape
    if type(self.shape)== Square:
      return self.get_area()//(shape.width**2)
    else:
      return self.get_area()//(shape.width*shape.height)


class Square(Rectangle):
  def __init__(self,width,height=None):
    self.width = width
    self.height = width

  def __str__(self):
    return f"Square(side={self.width})"
  
  def get_area(self):
      return self.width**2
  
  def set_side(self,width):
    self.width = width
    self.height = width