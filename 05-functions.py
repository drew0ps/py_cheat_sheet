"""
Python Functions Cheat Sheet

Covers:
- Defining functions
- Parameters and arguments
- Return values
- Default arguments
- Keyword arguments
- *args and **kwargs
- Lambda functions
- Scope
"""

# --- DEFINING A FUNCTION ---

def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))  # Hello, Alice!

# --- DEFAULT ARGUMENTS ---

def greet(name="World"):
    return f"Hello, {name}!"

print(greet())         # Hello, World
print(greet("Bob"))    # Hello, Bob

# --- KEYWORD ARGUMENTS ---

def describe_pet(animal, name):
    print(f"{name} is a {animal}.")

describe_pet(animal="dog", name="Buddy")  # Buddy is a dog.

# --- *args (VARIABLE NUMBER OF POSITIONAL ARGUMENTS) ---

def add_numbers(*args):
    return sum(args)

print(add_numbers(1, 2, 3))  # 6

# --- **kwargs (VARIABLE NUMBER OF KEYWORD ARGUMENTS) ---

def print_profile(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_profile(name="Alice", age=30, city="Zurich")

# --- RETURNING MULTIPLE VALUES ---

def stats(x, y):
    return x + y, x * y

s, p = stats(3, 4)
print("Sum:", s)     # Sum: 7
print("Product:", p) # Product: 12

# --- LAMBDA FUNCTIONS (ANONYMOUS FUNCTIONS) ---

square = lambda x: x * x
print(square(5))  # 25

# Use with map, filter, etc.
nums = [1, 2, 3, 4]
squared = list(map(lambda x: x ** 2, nums))
print(squared)  # [1, 4, 9, 16]

# --- NESTED FUNCTIONS & CLOSURE ---

def outer(msg):
    def inner():
        print(f"Message: {msg}")
    return inner

my_func = outer("Hello from inner function!")
my_func()

# --- SCOPE: LOCAL vs GLOBAL ---

x = 10  # global

def show_scope():
    x = 5  # local
    print("Inside:", x)

show_scope()         # Inside: 5
print("Outside:", x) # Outside: 10

# Modifying global inside function
def modify_global():
    global x
    x = 99

modify_global()
print("Modified global x:", x)  # Modified global x: 99
