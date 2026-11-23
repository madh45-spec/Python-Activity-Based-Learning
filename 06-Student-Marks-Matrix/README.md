# Case Study 6: Student Marks Matrix Analysis

## 1. Problem Statement

Educational institutions need to analyse students' marks across multiple subjects. Calculating individual totals, averages, and subject-wise performance manually can be time-consuming. This Python program uses a two-dimensional matrix to store marks and analyse student and subject performance.

## 2. Objectives

- To collect marks of multiple students across multiple subjects.
- To store marks using a two-dimensional list.
- To calculate individual student totals and averages.
- To calculate subject-wise averages.
- To identify the highest and lowest marks.

## 3. Assumptions

- The user enters the number of students and subjects.
- Marks are entered as numerical values.
- Each student has marks for the same number of subjects.
- The program assumes valid marks are entered.
- At least one student and one subject are provided.

## 4. Algorithm

1. Start the program.
2. Read the number of students and subjects.
3. Create an empty marks matrix.
4. Collect marks for every student.
5. Store each student's marks in a separate row.
6. Display the marks matrix.
7. Calculate and display each student's total and average.
8. Calculate and display each subject's average.
9. Find the highest and lowest marks in the matrix.
10. Display the overall summary.
11. Stop the program.

## 5. Flowchart

Start  
↓  
Enter number of students and subjects  
↓  
Create empty marks matrix  
↓  
Collect student marks  
↓  
Store marks in two-dimensional list  
↓  
Display marks matrix  
↓  
Calculate student totals and averages  
↓  
Calculate subject averages  
↓  
Find highest and lowest marks  
↓  
Display overall summary  
↓  
End

## 6. Pseudocode

BEGIN

INPUT number_of_students
INPUT number_of_subjects

CREATE empty marks matrix

FOR each student

    CREATE empty row

    FOR each subject

        INPUT mark
        ADD mark to row

    END FOR

    ADD row to marks matrix

END FOR

DISPLAY marks matrix

FOR each student

    total = SUM(student marks)
    average = total / number_of_subjects

    DISPLAY total and average

END FOR

FOR each subject

    total = 0

    FOR each student

        total = total + marks[student][subject]

    END FOR

    average = total / number_of_students

    DISPLAY subject average

END FOR

FIND highest and lowest marks

DISPLAY overall summary

END

## 7. Python Source Code

The Python program is saved in `marks_matrix.py`.

It uses variables, nested lists, nested loops, conditional statements, arithmetic operators, and comparison operators to analyse student marks.

## 8. Test Cases

| Test Case | Student | Subject 1 | Subject 2 | Subject 3 |
|---|---|---:|---:|---:|
| TC01 | Student 1 | 80 | 75 | 90 |
| TC02 | Student 2 | 65 | 85 | 70 |
| TC03 | Student 3 | 90 | 95 | 85 |

### Expected Results

- Student 1 Average: 81.67
- Student 2 Average: 73.33
- Student 3 Average: 90.00
- Subject 1 Average: 78.33
- Subject 2 Average: 85.00
- Subject 3 Average: 81.67
- Highest Mark: 95
- Lowest Mark: 65

## 9. Output Screenshots

Add screenshots of the successfully executed Python program in the `screenshots` folder.

## 10. Conclusion

The Student Marks Matrix Analysis program successfully stores and analyses marks using a two-dimensional list. It calculates student totals, individual averages, subject averages, and identifies the highest and lowest marks. This project demonstrates the practical application of Python nested lists, loops, and conditional statements.