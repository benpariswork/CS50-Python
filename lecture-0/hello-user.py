# Takes user's name as input and prints hello and the user name

# Ask user for their name
name = input("What is your name? ")

# Strip start/end whitespace from string name
name = name.strip()

# Apply title case
name = name.title()

# Print hello, NAME
print(f"hello, {name}")
