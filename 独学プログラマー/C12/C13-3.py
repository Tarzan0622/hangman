import math

class Triangle():
  def __init__(self, teihen, takasa):
    self.teihen = teihen
    self.takasa = takasa
  
  def triangle_menseki(self):
    return  self.teihen * self.takasa / 2

triangle_menseki1 = Triangle(2,3)
print(triangle_menseki1.triangle_menseki())
