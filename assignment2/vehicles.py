#parent class
class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print(f"{self.brand} {self.model}\nDriving")

class Car(Vehicle):
  #using pass to inherit everything in Vehicle
  pass

#plane class inheriting from Vehicle
class Plane(Vehicle):
  def move(self):
    print(f"{self.brand} {self.model} \nFlying")