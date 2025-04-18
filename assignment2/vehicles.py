class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Driving")

class Car(Vehicle):
  pass

class Plane(Vehicle):
  def move(self):
    print("Flying")