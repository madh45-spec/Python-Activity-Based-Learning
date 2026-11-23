# Case Study 8: Student Academic Risk Classification

## 1. Problem Statement

Educational institutions need to identify students who may face academic difficulties. Low marks and poor attendance can affect academic progress. This Python program analyses students' average marks and attendance percentages to classify their academic risk levels as High Risk, Medium Risk, or Low Risk.

## 2. Objectives

- To collect student academic details.
- To analyse average marks and attendance.
- To classify students based on academic risk.
- To identify students who may need academic support.
- To generate an academic risk summary.

## 3. Assumptions

- The user enters the number of students.
- Average marks and attendance are entered as percentages.
- Marks and attendance range from 0 to 100.
- Risk classification follows these conditions:
  - High Risk: Marks below 40 OR attendance below 60%.
  - Medium Risk: Marks below 60 OR attendance below 75%, provided the student is not High Risk.
  - Low Risk: Marks are 60 or above AND attendance is 75% or above.
- The classification is an educational exercise, not a formal assessment of a student's future.

## 4. Algorithm

1. Start the program.
2. Read the number of students.
3. Create an empty student list.
4. For each student:
   - Read the student's name.
   - Read average marks.
   - Read attendance percentage.
   - Classify the academic risk level.
   - Store the student details.
5. Display the academic risk report.
6. Count High Risk, Medium Risk, and Low Risk students.
7. Display the risk summary.
8. Stop the program.

## 5. Flowchart

Start  
↓  
Enter number of students  
↓  
Collect student details  
↓  
Enter marks and attendance  
↓  
Are marks below 40 OR attendance below 60?  
- Yes → High Risk
- No → Are marks below 60 OR attendance below 75?
  - Yes → Medium Risk
  - No → Low Risk

↓  
Store student details  
↓  
Display academic risk report  
↓  
Calculate risk summary  
↓  
Display summary  
↓  
End

## 6. Pseudocode

BEGIN

INPUT number_of_students

CREATE empty students list

FOR each student

    INPUT student_name
    INPUT average_marks
    INPUT attendance

    IF average_marks < 40 OR attendance < 60 THEN
        risk = "High Risk"

    ELSE IF average_marks < 60 OR attendance < 75 THEN
        risk = "Medium Risk"

    ELSE
        risk = "Low Risk"

    END IF

    ADD student details to students list

END FOR

DISPLAY academic risk report

SET high = 0
SET medium = 0
SET low = 0

FOR each student

    COUNT the student's risk category

END FOR

DISPLAY risk summary

END

## 7. Python Source Code

The Python program is saved in `academic_risk.py`.

It uses variables, lists, loops, conditional statements, logical operators, and comparison operators to classify students according to their academic performance.

## 8. Test Cases

| Test Case | Student | Average Marks | Attendance | Expected Risk |
|---|---|---:|---:|---|
| TC01 | Ravi | 35 | 80 | High Risk |
| TC02 | Priya | 55 | 85 | Medium Risk |
| TC03 | Arun | 80 | 90 | Low Risk |
| TC04 | Sneha | 70 | 65 | Medium Risk |

### Expected Summary

- Total Students: 4
- High Risk Students: 1
- Medium Risk Students: 2
- Low Risk Students: 1

## 9. Output Screenshots

Add screenshots of the successfully executed Python program in the `screenshots` folder.

## 10. Conclusion

The Student Academic Risk Classification program successfully analyses student marks and attendance to identify different academic risk levels. It generates individual risk reports and a summary of all students. This project demonstrates the practical use of Python lists, loops, conditional statements, and logical operators.