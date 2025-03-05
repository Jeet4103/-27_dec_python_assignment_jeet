# Parent class
class Vehicle:
    def type(self):
        return "This is a vehicle"

# Child class 1
class Car(Vehicle):
    def wheels(self):
        return "Cars have 4 wheels"

# Child class 2
class Bike(Vehicle):
    def wheels(self):
        return "Bikes have 2 wheels"

# Creating objects
car = Car()
bike = Bike()

print(car.type(), "-", car.wheels())
print(bike.type(), "-", bike.wheels())
