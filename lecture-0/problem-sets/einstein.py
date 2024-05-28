### E=mc^2
### In a file called einstein.py, implement a program in Python
### that prompts the user for mass as an integer (in kilograms)
### and then outputs the equivalent number of Joules as an integer.
### Assume that the user will input an integer.

# define main function to take mass input and call energy function
def main():
    m = int(input("Please provide mass in kilograms as an integer: "))
    print (energy(m))

# define custom function 'energy' to apply einstein's E=mc^2
def energy(x):
    joules = x * 300000000 * 300000000
    return joules

main()