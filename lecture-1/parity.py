# test input to see if it is even or odd

# define main function
def main():
    # take input for x as integer
    x = int(input("This program checks if a number is even or odd. Please provide a number to be checked: "))
    #call is_even function and pass x as param
    if is_even(x) is True:
        print("Even")
    else:
        print("Odd")

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

main()