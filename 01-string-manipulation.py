# Day 1 - String Manipulation

# String concatenation
print("String concatenation is done using the '+' sign.")
word = "tele" + "phone"
print(f"Example: 'tele' + 'phone' = {word}")

# Newlines and f-strings
print("\nNew lines can be created using a backslash and 'n': \\n")
print("f-strings allow you to embed variables inside strings using curly braces {}.")

print(f"\n{word}\nbooth")  # Adds a newline before "booth"

# User input and variable assignment
print("\nYou can assign user input to variables.")

hometown = input("What's the name of your hometown? ")
pet_name = input("What's the name of your pet? ")

# Create a band name by combining inputs
band_name = f"{hometown} {pet_name}"
print(f"\nYour band name could be: {band_name}")
