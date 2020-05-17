
class Square():
  def __init__(self, ippen):
    self.ippen=ippen
  
  def calculate_perimeter(self):
    return  self.ippen  * 4
  
  def change_size(self, new_size):
    self.ippen  +=  new_size

a_square  = Square(100)
print(a_square.ippen)

a_square.change_size(100)
print(a_square.ippen)