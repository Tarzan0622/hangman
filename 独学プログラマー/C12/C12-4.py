class Hexagon():
  def __init__(self, radius):
    self.radius = radius
  
  def seirokkakumennseki(self):
    return  self.radius * 6

a_hexagon = Hexagon(10)
print(a_hexagon.seirokkakumennseki())
