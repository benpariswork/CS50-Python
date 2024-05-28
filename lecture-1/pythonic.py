# copy of parity.py with pythonic example for parity function
# test input to see if it is even or odd

# define main function
def main():
    # take input for x as integer
    x = int(input("This program checks if a number is even or odd. Please provide a number to be checked: "))
    #call is_even function and pass x as param
    if is_even(x):
        print("Even")
    else:
        print("Odd")

# custom function tests for parity
def is_even(n):
    #return True if n % 2 == 0 else False
    return n % 2 == 0

main()