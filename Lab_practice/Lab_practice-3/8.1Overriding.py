class Animal:
    def speak(self):
        return "Animal makes a sound"

class Dog(Animal):
    def speak(self):  # Overriding the parent method
        return "Bark!"

class Cat(Animal):
    def speak(self):  # Overriding the parent method
        return "Meow!"

# Creating objects
dog = Dog()
cat = Cat()

print(dog.speak())  # Output: Bark!
print(cat.speak())  # Output: Meow!
