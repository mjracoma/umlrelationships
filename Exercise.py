#Exercise 1: Creating Person Class
#Exercise 2: Setting Age to private
#I added (\n) to the end of the age variable to make it more readable when printed out.
from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    @abstractmethod
    def role(self):
        pass

    def get_name(self):
        return (f"Name: {self.name}")
    def get_age(self):
        return (f"Age: {self.__age}\n ") #Making variables to private ensures that data won't be easily interchanged or modified by other parts of the program.

#Exercise 3: Inheritance
class Student(Person):
    def __init__(self, name,age):
        super().__init__(name, age)

    def role(self):
        return (f"{self.name} is a student.")

    def study(self):
        return (f"{self.name} is studying.\n ") 

student1 = Student("John", 20)
print(student1.get_name())
print(student1.get_age())
print(student1.role())
print(student1.study()) 

#Exercise 4: Create Teacher Class
class Teacher(Person):
    def __init__(self, name, age):
        super().__init__(name, age)

    def role(self):
        return (f"{self.name} is a teacher.")

    def teach(self):
        return (f"{self.name} is teaching.\n")

teacher1 = Teacher("Sir Abz", 40)
print(teacher1.get_name())
print(teacher1.get_age())
print(teacher1.role())
print(teacher1.teach()) 

#Exercise 5: Polymorphism 
#Exercise 6: Apply Abstraction on Person setting role() as an abstract method.