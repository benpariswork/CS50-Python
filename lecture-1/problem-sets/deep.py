### In deep.py, implement a program that prompts the user for the 
### answer to the Great Question of Life, the Universe and 
### Everything, outputting Yes if the user inputs 42 or 
### (case-insensitively) forty-two or forty two. Otherwise output No.

# define main function for input 
def main():
    #input
    x = input("What is the answer tothe Great Question of Life, the Universe, and Everything? ")
    #pass input to checker
    checker(x)

# define checker function
def checker(y):
    # remove whitespace and apply lowercase
    z = y.strip().lower()
    # compare z to 3 potential answers, output yes or no
    match z:
        case "42" | "forty two" | "forty-two":
            print("Yes")
        case _:
            print("No")

# call main function
main()