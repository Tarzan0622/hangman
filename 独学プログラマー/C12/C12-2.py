import math

class Circle():
  def __init__(self, radius):
    self.radius  = radius
  
  def area(self):
    return  self.radius **2 * math.pi

a_circle=Circle(4)
print(a_circle.area())
