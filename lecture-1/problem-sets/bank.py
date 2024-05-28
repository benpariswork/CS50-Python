### see problem here: https://cs50.harvard.edu/python/2022/psets/1/bank/

# define main function
def main():
    # take input for greeting as x
    x = input("Greeting: ")
    # print result for greeting_check function and pass x as param
    print(greeting_check(x))

# custom function tests greeting value
def greeting_check(g):
    # remove whitespace and apply lower case
    g = g.strip().lower()
    # if response starts with hello, return $0
    if g.startswith("hello"):
        return "$0"
    # if response starts with h, return $20
    elif g.startswith("h"):
        return "$20"
    # if response doesnt even start with h, return $100
    else:
        return "$100"

# call main
main()