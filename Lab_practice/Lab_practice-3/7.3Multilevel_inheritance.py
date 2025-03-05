# Grandparent class
class Grandparent:
    def family_name(self):
        return "Family Name: Smith"

# Parent class inheriting from Grandparent
class Parent(Grandparent):
    def parent_trait(self):
        return "Parent Trait: Hardworking"

# Child class inheriting from Parent
class Child(Parent):
    def child_trait(self):
        return "Child Trait: Intelligent"

# Creating an object
child = Child()
print(child.family_name())
print(child.parent_trait())
print(child.child_trait())
