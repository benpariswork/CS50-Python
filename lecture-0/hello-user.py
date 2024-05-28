# Takes user's name as input and prints hello and the user name

# # Ask user for their name
# # Strip start/end whitespace from string name and apply title case
# name = input("What is your name? ").strip().title()

# # Print hello, NAME
# print(f"hello, {name}")

def main():

    # output using custom function
    name = input("What's your name? ").strip().title()
    hello(name)

    # output with default 'to' variable
    hello()

# Custom function to say hello
def hello(to="world"):
    print("hello,", to)

main()