"""
Python OOP Cheat Sheet

Core OOP Concepts in Python:
- Class
- Object
- Constructor (__init__)
- Attributes
- Methods
- Inheritance
- Encapsulation
- Polymorphism
"""

# --- DEFINING A CLASS ---

class Animal:
    # Constructor
    def __init__(self, name):
        self.name = name  # Attribute

    # Method
    def speak(self):
        return f"{self.name} makes a sound."

# --- CREATING AN OBJECT ---

dog = Animal("Dog")
print(dog.speak())  # Dog makes a sound.

# --- INHERITANCE ---

class Dog(Animal):  # Dog inherits from Animal
    def speak(self):
        return f"{self.name} barks."

buddy = Dog("Buddy")
print(buddy.speak())  # Buddy barks.

# --- ENCAPSULATION ---

class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age  # Private attribute

    def get_age(self):     # Getter
        return self.__age

    def set_age(self, new_age):  # Setter
        if new_age > 0:
            self.__age = new_age

p = Person("Alice", 30)
print(p.name)           # Alice
print(p.get_age())      # 30
p.set_age(35)
print(p.get_age())      # 35

# --- POLYMORPHISM ---

class Cat(Animal):
    def speak(self):
        return f"{self.name} meows."

def animal_sound(animal):
    print(animal.speak())

animal_sound(Dog("Max"))   # Max barks.
animal_sound(Cat("Luna"))  # Luna meows.

# --- CLASS vs INSTANCE ATTRIBUTES ---

class Counter:
    count = 0  # Class attribute

    def __init__(self):
        Counter.count += 1

print(Counter.count)  # 0
a = Counter()
b = Counter()
print(Counter.count)  # 2

# --- STATIC METHODS & CLASS METHODS ---

class MathTools:
    @staticmethod
    def add(x, y):
        return x + y

    @classmethod
    def description(cls):
        return f"This is {cls.__name__} class"

print(MathTools.add(5, 3))         # 8
print(MathTools.description())     # This is MathTools class
