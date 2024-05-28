### See problem here: https://cs50.harvard.edu/python/2022/psets/1/interpreter/

# define main function
def main():
    # take input math
    math = input("Please provide x, y, and z. x and z should be integers and y should be an operator, put spaces inbetween each. i.e. '5 + 6' ")
    # split math into 3 strings
    math = math.split()
    x, y, z = math
    # change x and z into floats
    x = float(x)
    z = float(z)
    # call int, send 2 floats and 1 str to int function, print return value
    print(int(x, y, z))
    

# define int function
def int(a, b, c):
    # match y with operator and calculate answer
    match b:
        case "+":
            return a + c
        case "-":
            return a - c
        case "*":
            return a * c
        case "/":
            return a / c

# call main
main()