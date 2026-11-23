print("==========================================")
print("      STUDENT PERFORMANCE ANALYSIS")
print("==========================================")

n = int(input("\nEnter number of students: "))

students = []

# Collect student details
for i in range(n):

    print("\nEnter details of Student", i + 1)

    name = input("Enter student name: ")

    marks = []

    for j in range(3):
        mark = float(input("Enter marks for Exam " + str(j + 1) + ": "))
        marks.append(mark)

    average = sum(marks) / len(marks)

    if average >= 75:
        performance = "Excellent"

    elif average >= 60:
        performance = "Good"

    elif average >= 40:
        performance = "Average"

    else:
        performance = "Needs Improvement"

    trend = marks[2] - marks[0]

    if trend > 0:
        trend_status = "Improving"

    elif trend < 0:
        trend_status = "Declining"

    else:
        trend_status = "Stable"

    students.append([name, marks, average, performance, trend_status])


# Display performance report
print("\n========== STUDENT PERFORMANCE REPORT ==========")

for student in students:

    print("\nStudent Name:", student[0])
    print("Exam Marks:", student[1])
    print("Average Marks:", round(student[2], 2))
    print("Performance:", student[3])
    print("Performance Trend:", student[4])


# Calculate class average
total_average = 0

for student in students:
    total_average += student[2]

if len(students) > 0:
    class_average = total_average / len(students)
else:
    class_average = 0


print("\n========== CLASS SUMMARY ==========")

print("Total Students:", len(students))
print("Class Average:", round(class_average, 2))

print("\n==========================================")
print("       ANALYSIS COMPLETED")
print("==========================================")