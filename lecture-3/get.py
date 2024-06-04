def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            x = int(input("What is x? "))
        except ValueError:
            print("x is not an integer, please input x as an integer ")
        else:
            break
    return x

if __name__ == "__main__":
    main()