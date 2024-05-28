### See problem set here: https://cs50.harvard.edu/python/2022/psets/1/extensions/

## Program will take a file name as input and export media type

# Define main function, take an input, sanitize, and send to ext function
def main():
    name = input("This program will return media type, what is the name of your file? ")
    name = name.strip().lower()
    print(ext(name))

# take sanitized file name and output one of 6 media types or 'application/octet-stream'
def ext(x):
    if x.endswith(".jpg") or x.endswith(".jpeg"):
        return "image/jpeg"
    elif x.endswith(".gif"):
        return "image/gif"
    elif x.endswith(".png"):
        return "image/png"
    elif x.endswith(".pdf"):
        return "application/pdf"
    elif x.endswith(".txt"):
        return "text/plain"
    elif x.endswith(".zip"):
        return "application/zip"
    else:
        return "application/octet-stream"

# calls main function
main()