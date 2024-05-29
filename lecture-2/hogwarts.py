# students = ["Hermoine", "Harry", "Ron"]

# print(students[0])
# print(students[1])
# print(students[2])

### for loop
# for student in students:
#     print(student)

### print list with nums
# for i in range(len(students)):
#     print(i + 1, students[i])

students = {
    "Hermoine": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin",
}

# print(students["Hermoine"])
# print(students["Harry"])
# print(students["Ron"])
# print(students["Draco"])
for student in students:
    print(student, students[student], sep=", ")


