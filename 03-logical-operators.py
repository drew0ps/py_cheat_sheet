"""
Python Logical Operators Cheat Sheet

Logical operators are used to combine conditional statements.
They return Boolean values: True or False.

Operators:
- and
- or
- not
"""

# --- EXAMPLES ---

a = True
b = False

# AND: Returns True if both statements are True
print("a and b:", a and b)  # False

# OR: Returns True if at least one statement is True
print("a or b:", a or b)    # True

# NOT: Reverses the result
print("not a:", not a)      # False
print("not b:", not b)      # True

# --- COMBINED CONDITIONS ---

x = 5
y = 10

print("\nCombined numeric conditions:")
print("x > 0 and y > 0:", x > 0 and y > 0)   # True
print("x < 0 or y > 0:", x < 0 or y > 0)     # True
print("not (x > 0):", not (x > 0))           # False

# --- IN CONDITIONALS ---

print("\nConditional usage:")

if x > 0 and y > 0:
    print("Both x and y are positive.")

if x < 0 or y > 0:
    print("At least one of x or y is positive.")

if not (x > 0):
    print("x is NOT greater than 0.")
else:
    print("x IS greater than 0.")
