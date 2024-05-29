### see problem here: https://cs50.harvard.edu/python/2022/psets/2/camel/

def main():
    c = input("please provide a camel string ")
    print(camel_to_snake(c))

def camel_to_snake(camel_str):
    # initialize an empty list to store the new characters
    char_list = []
    
    # iterate over each character in the input string
    for char in camel_str:
        # if the current character is uppercase add an underscore before it
        if char.isupper():
            char_list.append("_")
        # add the current character to the new string list
        char_list.append(char)
    
    # join the list of characters into a single string and return it
    snake_upper = "".join(char_list)
    return snake_upper.lower()

if __name__ == "__main__":
    main()