print("==========================================")
print("    STUDENT TIMETABLE CONFLICT DETECTOR")
print("==========================================")

n = int(input("\nEnter number of classes: "))

classes = []

# Collect class details
for i in range(n):

    print("\nEnter details of Class", i + 1)

    subject = input("Enter subject name: ")
    day = input("Enter day: ").lower()
    start = int(input("Enter starting hour (0-23): "))
    end = int(input("Enter ending hour (0-23): "))

    if start < 0 or end > 23 or start >= end:
        print("Invalid time! Class skipped.")
        continue

    classes.append([subject, day, start, end])


# Check timetable conflicts
print("\n========== TIMETABLE CONFLICT REPORT ==========")

conflicts = 0

for i in range(len(classes)):

    for j in range(i + 1, len(classes)):

        class1 = classes[i]
        class2 = classes[j]

        if class1[1] == class2[1]:

            if class1[2] < class2[3] and class2[2] < class1[3]:

                print("\nConflict Detected!")
                print("Subject 1:", class1[0])
                print("Subject 2:", class2[0])
                print("Day:", class1[1])

                conflicts += 1


# Display final result
print("\n========== TIMETABLE SUMMARY ==========")

print("Total Classes:", len(classes))
print("Total Conflicts:", conflicts)

if conflicts == 0:
    print("No timetable conflicts found.")

else:
    print("Please revise the timetable.")


print("\n==========================================")
print("       ANALYSIS COMPLETED")
print("==========================================")