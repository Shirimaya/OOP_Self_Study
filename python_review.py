#Object Oriented Programming

#name class
class Dog:
    #methods
    #special definition to instantiate the method
    def __init__(self, name, age):
        self.name = name
        self.age = age      

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def add_one(self, x):
        return x + 1

    def bark(self):
        print ("bark")

d = Dog("Stephen", 30)
print(d.get_name())
print(d.get_age())

