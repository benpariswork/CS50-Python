### see problem here: https://cs50.harvard.edu/python/2022/psets/1/meal/

# define main
def main():
    # take time as input and assign to t
    time = input("Please provide a 24 hr time in the format of '#:##' or '##:##' ")
    hours = convert(time)
    check(hours)


def convert(x):
    # split var time into two strings
    x = x.split(":")
    # assign strings to var a and b
    h, m = x
    # change a and b to floats
    h = float(h)
    m = float(m)
    # calculate hours and assign to var hours
    hours = h + (m / 60)
    return hours

def check(y):
    if 7.0 <= y <= 8.0:
        print("breakfast time")
    if 12.0 <= y <= 13.0:
        print("lunch time")        
    if 18.0 <= y <= 19.0:
        print("dinner time")

if __name__ == "__main__":
    main()