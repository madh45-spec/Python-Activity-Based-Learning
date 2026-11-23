print("====================================")
print("   UNIVERSITY SCHOLARSHIP SYSTEM")
print("====================================")

print("Welcome to the Scholarship Allocation Program!")

n = int(input("\nEnter the number of scholarship applicants: "))

students = []

# Collect student details
for i in range(n):

    print("\nEnter details of Student", i + 1)

    name = input("Enter student name: ")

    marks = []

    for j in range(5):
        mark = float(input("Enter marks for Subject " + str(j + 1) + ": "))
        marks.append(mark)

    attendance = float(input("Enter attendance percentage: "))
    income = float(input("Enter annual family income in rupees: "))

    total = sum(marks)
    average = total / len(marks)

    if average >= 75 and min(marks) >= 60 and attendance >= 75 and income <= 250000:
        eligibility = "Eligible"
    else:
        eligibility = "Not Eligible"

    students.append([name, marks, attendance, income, average, eligibility])


# Display all student results
print("\n========== SCHOLARSHIP RESULTS ==========")

for student in students:

    print("\nStudent Name:", student[0])
    print("Subject Marks:", student[1])
    print("Average Marks:", student[4])
    print("Attendance:", student[2], "%")
    print("Family Income: Rs.", student[3])
    print("Scholarship Status:", student[5])


# Select eligible students
eligible_students = []

for student in students:
    if student[5] == "Eligible":
        eligible_students.append(student)


# Rank eligible students
eligible_students.sort(key=lambda student: (-student[4], -student[2], student[3]))


# Display merit list
print("\n========== SCHOLARSHIP MERIT LIST ==========")

if len(eligible_students) == 0:

    print("No students are eligible for the scholarship.")

else:

    for i in range(len(eligible_students)):

        student = eligible_students[i]

        print("\nRank:", i + 1)
        print("Student Name:", student[0])
        print("Average Marks:", student[4])
        print("Attendance:", student[2], "%")
        print("Family Income: Rs.", student[3])

print("\n====================================")
print("       PROGRAM COMPLETED")
print("====================================")