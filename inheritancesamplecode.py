class Vehicle:
    def __init__(self, brand):
        self.brand = brand


class Car(Vehicle):
    def honk(self):
        return f"{self.brand} says Beep!"
    
    