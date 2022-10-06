#OOP
#General Class
class Pet:
    def __init__ (self, name, age):
        self.name = name
        self.age = age
    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")
    def speak(self):
        print("I Don't know what to say")
#Specific Class
class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def speak(self):
        print("Meow")

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old and I am {self.color}")
#Specific Class
class Dog(Pet):
    def speak(self):
        print("Bark")
#Specific Class
class Fish(Pet):
    pass

p = Pet("Tim", 19)
p.show()
p.speak()
c = Cat("Bill",34, "Brown")
c.show()
c.speak()
d = Dog("Jill",30)
d.show()
d.speak()
e = Fish("Banana", 30)
e.show()
e.speak()