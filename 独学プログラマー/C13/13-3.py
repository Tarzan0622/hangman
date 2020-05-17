class Shape():
  def what_i_am(self):
    print("I  am  a shape.")

class Rectangle(Shape):
  def __init__(self, tate, yoko):
    self.tate=tate
    self.yoko=yoko
  
  def calculate_perimeter(self):
    return self.tate  * 2 + self.yoko * 2
  
class Square(Shape):
  def __init__(self, ippen):
    self.ippen=ippen
  
  def calculate_perimeter(self):
    return  self.ippen  * 4

a_rectangle = Rectangle(20, 50)
a_square  = Square(30)

a_rectangle.what_i_am()
a_square.what_i_am()
