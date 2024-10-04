"""
OOPs: Object Oriented Programming

class:
A user defined data type and it is blue print of an object.
or It is a logical inference of an object.
Attributes and Actions/ States and Behaviours/ Variables and Methods
Object:
An object is an instance of a class, which means it is created based on the structure defined by the class.

If any language in programming is called as OOP language, it should satisfy the below concepts:
1. Encapsulation
2. Abstraction
3. Inheritance
4. Polymorphism

1. Encapsulation:
---------------
Binding the data members(Fields,Variables,Attributes) & member methods(Methods(IM,CM,SM)) into single entity.

2. Abstraction :
--------------
Hiding the implementation details in the methods of a class from the real world.

In a "Normal class" Abstraction is 0%
In "Abstract Class" Abstraction is 0-100 %
In an "Interface"   Abstraction is 100%

3. Inheritance:
---------------
The new class is called derived (or child) class and the one from which it inherits is called the base (or parent) class

4. Polymorphism:
---------------
    - Static Polymorphism -- Method overloading
    - Dynamic Polymorphism -- Method overriding
"""


class Pet:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def eat(self):
        print(f"{self.name} is eating food.")

    def play(self):
        print(f"{self.name} is play with toys")

    def sleep(self):
        print(f"{self.name} is sleeping on bed.")

    def __str__(self):
        return f"{self.name} has age of {self.age} years and having weight: {self.weight}kg"


puppy = Pet("Puppy", 3, 10)
puppy.eat()
print(puppy)

