class Animal(object):
    pass

class Dog(Animal):
    def __init__(self,name):
        self.name = name
        
class Cat(Animal):
    def __init__(self,name):
        self.name = name
        
class Person(object):
    def __init__(self,name):
        self.name = name
        self.pet = None
        
class Employee(Person):
    def __init__(self,name,salary):
    # super() lets you avoid referring to the parent class explicitly
    # the main advantage comes with multiple inheritance, where all sorts of fun stuff can happen
    # in Python 3.0, you can just use super().__init__(), no need to mention parent class or current class
        super(Employee, self).__init__(name)
        self.salary = salary

class Fish(object):
    pass

class Salmon(Fish):
    pass
    
class Halibut(Fish):
    pass
    
rover = Dog("Rover")

satan = Cat("Satan")

mary = Person("Mary")

mary.pet = satan

frank = Employee("Frank", 120000)

frank.pet = rover

fliper = Fish()

crouse = Salmon()

harry = Halibut()

    