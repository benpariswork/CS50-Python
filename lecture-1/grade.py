#set var score to input
score = int(input("Score: "))

#output grade based on var score
if score >= 101:
    print("Grade: A+, good work.")
elif score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")