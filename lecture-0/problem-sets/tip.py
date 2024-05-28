### Finish program by writting the following to functions:
#### dollars_to_float, which should accept a str as input 
##### (formatted as $##.##, wherein each # is a decimal digit), 
##### remove the leading $, and return the amount as a float. 
##### For instance, given $50.00 as input, it should return 50.0
#### percent_to_float, which should accept a str as input 
##### (formatted as ##%, wherein each # is a decimal digit), 
##### remove the trailing %, and return the percentage as a float.
##### For instance, given 15% as input, it should return 0.15.

# main is provided in problem set
def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

# define function to get a float for cost
def dollars_to_float(d):
    # remove $
    ds = d.strip("$")
    # change from str to float
    df = float(ds)
    #return float
    return df
    
# define function to get a float for percent
def percent_to_float(p):
    #remove %
    ps = p.strip("%")
    #change str to float and divide by 100 (to make percentage of 1)
    pf = float(ps) / 100
    #return percent float
    return pf


main()
