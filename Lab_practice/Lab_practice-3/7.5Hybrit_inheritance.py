# Base class
class Person:
    def info(self):
        return "This is a person"

# Parent class 1
class Employee(Person):
    def work(self):
        return "Employee is working"

# Parent class 2
class Student(Person):
    def study(self):
        return "Student is studying"

# Child class inheriting from both Employee and Student (Multiple + Hierarchical)
class Intern(Employee, Student):
    def role(self):
        return "Intern is learning and working"

# Creating an object
intern = Intern()
print(intern.info())
print(intern.work())
print(intern.study())
print(intern.role())
