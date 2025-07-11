"""
Python Cheat Sheet: if Statements and for Loops

Covers:
- if, elif, else
- Comparison operators
- Logical operators
- Nested ifs
- for loops with ranges, lists, strings
- break and continue
"""

# --- IF STATEMENTS ---

print("== IF STATEMENTS ==")

age = 18

if age >= 18:
    print("You are an adult.")
elif age >= 13:
    print("You are a teenager.")
else:
    print("You are a child.")

# --- COMPARISON OPERATORS ---
# >, <, >=, <=, ==, !=

x = 10
y = 20

if x != y:
    print("x and y are not equal")

# --- LOGICAL OPERATORS ---
# and, or, not

has_ticket = True
is_sober = True

if has_ticket and is_sober:
    print("You may enter the concert.")

# --- NESTED IF STATEMENTS ---

temperature = 30

if temperature > 20:
    print("It's warm.")
    if temperature > 35:
        print("It's really hot!")
else:
    print("It's cool or cold.")

# --- FOR LOOPS ---

print("\n== FOR LOOPS ==")

# Loop through a list
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(f"I like {fruit}")

# Loop through a string
for char in "Hello":
    print(char)

# Loop with range()
for i in range(5):
    print(f"Number: {i}")  # 0 to 4

# Loop with custom range
for i in range(2, 10, 2):  # start, stop, step
    print(f"Even number: {i}")  # 2, 4, 6, 8

# --- BREAK AND CONTINUE ---

print("\n== BREAK AND CONTINUE ==")

# Break: exit the loop early
for num in range(1, 6):
    if num == 3:
        print("Breaking at 3")
        break
    print(num)

# Continue: skip current iteration
for num in range(1, 6):
    if num == 3:
        print("Skipping 3")
        continue
    print(num)

# --- NESTED FOR LOOPS ---

print("\n== NESTED LOOPS ==")

for i in range(1, 4):
    for j in range(1, 4):
        print(f"i={i}, j={j}")
