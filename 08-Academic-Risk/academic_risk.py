print("==========================================")
print("      STUDENT ACADEMIC RISK SYSTEM")
print("==========================================")

n = int(input("\nEnter number of students: "))

students = []

# Collect student details
for i in range(n):

    print("\nEnter details of Student", i + 1)

    name = input("Enter student name: ")

    marks = float(input("Enter average marks (0-100): "))
    attendance = float(input("Enter attendance percentage (0-100): "))

    # Classify academic risk
    if marks < 40 or attendance < 60:
        risk = "High Risk"

    elif marks < 60 or attendance < 75:
        risk = "Medium Risk"

    else:
        risk = "Low Risk"

    students.append([name, marks, attendance, risk])


# Display student risk report
print("\n========== ACADEMIC RISK REPORT ==========")

for student in students:

    print("\nStudent Name:", student[0])
    print("Average Marks:", student[1])
    print("Attendance:", student[2], "%")
    print("Academic Risk:", student[3])


# Calculate risk summary
high = 0
medium = 0
low = 0

for student in students:

    if student[3] == "High Risk":
        high += 1

    elif student[3] == "Medium Risk":
        medium += 1

    else:
        low += 1


# Display summary
print("\n========== RISK SUMMARY ==========")

print("Total Students:", len(students))
print("High Risk Students:", high)
print("Medium Risk Students:", medium)
print("Low Risk Students:", low)

print("\n==========================================")
print("       ANALYSIS COMPLETED")
print("==========================================")