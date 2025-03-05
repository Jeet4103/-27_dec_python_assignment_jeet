# Parent class 1
class Father:
    def skill(self):
        return "Father's skill: Gardening"

# Parent class 2
class Mother:
    def talent(self):
        return "Mother's talent: Singing"

# Child class inheriting from both Father and Mother
class Child(Father, Mother):
    def hobby(self):
        return "Child's hobby: Painting"

# Creating an object
child = Child()
print(child.skill())
print(child.talent())
print(child.hobby())
