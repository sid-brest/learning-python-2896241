#
# Example file for working with classes
# LinkedIn Learning Python course by Joe Marini
#
class Vehicle():
    def __init__(self, style):
        self.style = style
    
    def __init__(self, speed):
        self.speed = speed

class Car(Vehicle):
    def __init__(self, engine):
        super().__init__("Car")
        self.wheels = 4
        self.doors = 4
        self.engine = engine

Car1 = Car("Gas")
Car2 = Car("Electric")

print(Car1.engine)
print(Car2.engine)

print(Car1.doors)
print(Car2.doors)



 