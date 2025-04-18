from vehicles import Car, Plane
while True:
    brand = input("Brand Name: ")
    model = input("Model: ")
    
    car = Car(brand, model)
    
    plane = Plane(brand, model)
    
    car.move()
    
    plane.move()