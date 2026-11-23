# Case Study 1: University Scholarship Allocation System

## 1. Problem Statement

Universities receive scholarship applications from many students. Manually checking academic performance, attendance, and family income can be time-consuming and may lead to errors.

The University Scholarship Allocation System is a Python-based program that collects student details, calculates academic averages, checks scholarship eligibility, and generates a merit list by ranking eligible students.

## 2. Objectives

1. Collect student information and subject marks.
2. Calculate total and average marks.
3. Check scholarship eligibility based on academic performance.
4. Verify attendance and annual family income.
5. Identify eligible students.
6. Generate a merit-based ranking list.

## 3. Assumptions

1. Each student has five subjects.
2. The minimum required average is 75%.
3. Every subject must have at least 60 marks.
4. Minimum attendance is 75%.
5. Annual family income must not exceed ₹2,50,000.
6. Students are ranked by average marks, attendance, and family income.
7. These eligibility thresholds are assumed for this case study.
## 4. Algorithm

1. Start the program.
2. Display the University Scholarship System heading.
3. Read the number of scholarship applicants.
4. Create an empty list to store student details.
5. For each student:
   - Read the student's name.
   - Read marks in five subjects.
   - Read attendance percentage.
   - Read annual family income.
   - Calculate total marks.
   - Calculate average marks.
   - Check whether the student satisfies all scholarship eligibility conditions.
   - Store the student's details and eligibility status.
6. Display the results of all students.
7. Create a separate list containing only eligible students.
8. Sort eligible students based on:
   - Higher average marks.
   - Higher attendance.
   - Lower family income.
9. Generate and display the scholarship merit list.
10. If no student is eligible, display an appropriate message.
11. Display the program completion message.
12. Stop.
## 5. Flowchart

The flowchart represents the sequence of operations performed by the University Scholarship Allocation System.

**Flow:**

Start → Enter Number of Students → Collect Student Details → Calculate Average → Check Eligibility → Store Student Status → Check for Remaining Students → Sort Eligible Students → Generate Merit List → Display Results → Stop.
## 6. Pseudocode

BEGIN

DISPLAY "UNIVERSITY SCHOLARSHIP SYSTEM"

INPUT number_of_students

CREATE empty list students

FOR each student:

    INPUT student_name

    CREATE empty list marks

    FOR each of five subjects:

        INPUT subject_marks

        ADD subject_marks to marks

    END FOR

    INPUT attendance_percentage

    INPUT annual_family_income

    CALCULATE total_marks

    CALCULATE average_marks

    IF average_marks >= 75 AND minimum_marks >= 60
       AND attendance >= 75 AND family_income <= 250000 THEN

        SET eligibility = "Eligible"

    ELSE

        SET eligibility = "Not Eligible"

    END IF

    STORE student details in students

END FOR

DISPLAY all student results

CREATE empty list eligible_students

FOR each student in students:

    IF student is eligible THEN

        ADD student to eligible_students

    END IF

END FOR

SORT eligible_students BY:

    1. Higher average marks
    2. Higher attendance
    3. Lower family income

IF eligible_students is empty THEN

    DISPLAY "No students are eligible"

ELSE

    DISPLAY scholarship merit list

END IF

DISPLAY "PROGRAM COMPLETED"

END
## 7. Python Source Code

The University Scholarship Allocation System is implemented using Python.

The program uses the following concepts:

1. Variables and data types – to store student information.
2. Lists – to store student records.
3. Nested lists – to store subject marks and student details.
4. For loops – to collect and process student information.
5. Conditional statements – to check scholarship eligibility.
6. Logical operators – to combine eligibility conditions.
7. Built-in functions – `sum()`, `min()`, and `len()`.
8. List operations – `append()` and `sort()`.
9. List indexing – to retrieve individual student details.

**Source file:** `scholarship.py`

The complete executable source code is available in the project folder.
## 8. Test Cases

| Test Case | Average Marks | Minimum Subject Mark | Attendance | Family Income | Expected Result |
|---|---:|---:|---:|---:|---|
| TC01 | 88 | 80 | 90% | ₹2,00,000 | Eligible |
| TC02 | 75 | 65 | 75% | ₹2,50,000 | Eligible |
| TC03 | 70 | 65 | 90% | ₹2,00,000 | Not Eligible |
| TC04 | 85 | 55 | 90% | ₹2,00,000 | Not Eligible |
| TC05 | 90 | 80 | 70% | ₹2,00,000 | Not Eligible |
| TC06 | 85 | 80 | 90% | ₹3,00,000 | Not Eligible |

### Test Case Analysis

- TC01: Student satisfies all eligibility conditions.
- TC02: Student satisfies all conditions at the minimum thresholds.
- TC03: Average marks are below 75%.
- TC04: One subject mark is below 60.
- TC05: Attendance is below 75%.
- TC06: Family income exceeds ₹2,50,000.

**Result:** The program correctly checks the scholarship eligibility conditions for the given test scenarios.
## 9. Conclusion

The University Scholarship Allocation System was successfully developed using Python.

The program collects student details, calculates total and average marks, checks academic performance, attendance, and family income, and identifies eligible students.

It also generates a merit list by ranking eligible students based on academic performance, attendance, and family income.

Through this project, concepts such as variables, data types, loops, conditional statements, logical operators, lists, nested lists, and built-in functions were applied practically.

The project demonstrates how Python programming can simplify scholarship allocation and reduce manual effort.