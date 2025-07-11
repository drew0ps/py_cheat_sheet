# Day 2 - Integer Manipulation in Python

# --- What is an Integer? ---
# Integers are whole numbers (positive, negative, or zero)
print("Examples of integers:")
print(42)      # Positive integer
print(-7)      # Negative integer
print(0)       # Zero is also an integer

# --- Basic Arithmetic with Integers ---

print("\nInteger addition (+):")
a = 5 + 3
print(f"5 + 3 = {a}")

print("\nInteger subtraction (-):")
b = 10 - 4
print(f"10 - 4 = {b}")

print("\nInteger multiplication (*):")
c = 6 * 7
print(f"6 * 7 = {c}")

print("\nInteger division (/):")
d = 20 / 4
print(f"20 / 4 = {d}  (returns float)")

print("\nFloor division (//):")
e = 20 // 3
print(f"20 // 3 = {e}  (returns whole number without remainder)")

print("\nModulus (%):")
f = 20 % 3
print(f"20 % 3 = {f}  (returns remainder)")

print("\nExponentiation (**):")
g = 2 ** 3
print(f"2 ** 3 = {g}  (2 to the power of 3)")

# --- Type Conversion ---

print("\nConverting string to integer using int():")
num_str = "123"
num = int(num_str)
print(f"Converted '{num_str}' to {num}")

print("\nConverting float to integer using int():")
flt = 12.34
flt_to_int = int(flt)
print(f"Converted {flt} to {flt_to_int} (truncates decimal)")

# --- Type Checking ---

print("\nChecking variable types with type():")
print(f"type(a): {type(a)}")
print(f"type(num): {type(num)}")
print(f"type(flt_to_int): {type(flt_to_int)}")

# --- Combining Arithmetic ---

print("\nPerforming multiple operations:")
x = 15
y = 4
print(f"x = {x}, y = {y}")
print(f"Sum: {x + y}")
print(f"Difference: {x - y}")
print(f"Product: {x * y}")
print(f"Division: {x / y}")

# --- User Input with Integers ---

print("\nGetting integer input from the user:")
user_input = input("Enter a number: ")
user_number = int(user_input)
print(f"You entered: {user_number}")

print("\nPerforming arithmetic with user input:")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
total = num1 + num2
print(f"The sum of {num1} and {num2} is: {total}")
