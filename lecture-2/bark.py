def main():
    bark(get_number())

def get_number():
    while True:
        n = int(input("what is n? "))
        if n > 1:
            return n

def bark(n):
    for _ in range (n):
        print("bark")

if __name__ == "__main__":
    main()