class Horse():
  def __init__(self,name,owner):
    self.name = name
    self.owner  = owner

class Rider():
  def __init__(self, name):
    self.name = name

taka  = Rider("Tarzan")
victory = Horse("Victory",taka)

print(victory.owner.name)
