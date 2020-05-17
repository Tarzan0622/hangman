class Rectangle():
  def __init__(self, tate, yoko):
    self.tate=tate
    self.yoko=yoko
  
  def calculate_perimeter(self):
    return self.tate  * 2 + self.yoko * 2
  
class Square():
  def __init__(self, ippen):
    self.ippen=ippen
  
  def calculate_perimeter(self):
    return  self.ippen  * 4

a_rectangle = Rectangle(5,10)
a_square  = Square(10)

print(a_rectangle.calculate_perimeter())
print(a_square.calculate_perimeter())
