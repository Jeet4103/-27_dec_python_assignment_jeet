# Parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Animal makes a sound"

# Child class
class Dog(Animal):
    def speak(self):
        return "Bark!"

# Creating an object
dog = Dog("Buddy")
print(f"{dog.name} says: {dog.speak()}")
