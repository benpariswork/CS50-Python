# def main():
#     print_column(3)
#     print_row(6)

# def print_column(height):
#     for _ in range(height):
#         print("#")

# def print_row(width):
#     print("?" * width)


def main():
    print_square(3)

## !!!not a fan of this one
# def print_square(size):

#     # For each row in square
#     for i in range(size):

#         # For each brick in row
#         for j in range(size):

#             #  Print brick
#             print("#", end="")

#         # Print blank line
#         print()

def main():
    print_square(3)


def print_square(size):
    for i in range(size):
        print_row(size)


def print_row(width):
    print("#" * width)


if __name__ == "__main__":
    main()
