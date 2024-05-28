### In a file called playback.py, implement a program in
### Python that prompts the user for input and then outputs
### that same input, replacing each space with ... 
### (i.e., three periods).

#take input to be transformed
fast = input("Provide a sentence for transformation ")

#replace spaces with ellipses
slow = fast.replace(" ", "...")

#print result
print(slow)