print("==========================================")
print("       STUDENT MARKS MATRIX ANALYSIS")
print("==========================================")

students = int(input("Enter number of students: "))
subjects = int(input("Enter number of subjects: "))

marks = []

# Collect marks
for i in range(students):

    print("\nEnter marks for Student", i + 1)

    row = []

    for j in range(subjects):

        mark = float(input("Enter marks for Subject " + str(j + 1) + ": "))
        row.append(mark)

    marks.append(row)


# Display marks matrix
print("\n========== STUDENT MARKS MATRIX ==========")

for i in range(students):

    print("Student", i + 1, ":", marks[i])


# Calculate student totals and averages
print("\n========== STUDENT PERFORMANCE ==========")

for i in range(students):

    total = sum(marks[i])
    average = total / subjects

    print("\nStudent", i + 1)
    print("Total Marks:", total)
    print("Average Marks:", round(average, 2))


# Calculate subject averages
print("\n========== SUBJECT PERFORMANCE ==========")

for j in range(subjects):

    total = 0

    for i in range(students):
        total += marks[i][j]

    average = total / students

    print("Subject", j + 1, "Average:", round(average, 2))


# Find highest and lowest marks
highest = marks[0][0]
lowest = marks[0][0]

for i in range(students):

    for j in range(subjects):

        if marks[i][j] > highest:
            highest = marks[i][j]

        if marks[i][j] < lowest:
            lowest = marks[i][j]


print("\n========== OVERALL SUMMARY ==========")

print("Highest Mark:", highest)
print("Lowest Mark:", lowest)

print("\n==========================================")
print("       ANALYSIS COMPLETED")
print("==========================================")