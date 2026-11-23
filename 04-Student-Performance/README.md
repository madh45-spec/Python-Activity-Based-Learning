# Case Study 4: Student Performance Trend Analysis

## 1. Problem Statement

Educational institutions need to monitor students' academic performance over multiple examinations. This Python program collects marks from three exams, calculates student averages, identifies performance levels, and determines whether a student's performance is improving, declining, or stable.

## 2. Objectives

- To collect student names and examination marks.
- To calculate average marks.
- To classify student performance.
- To identify performance trends.
- To calculate the overall class average.

## 3. Assumptions

- Each student has marks from three examinations.
- Marks are entered as numerical values.
- Average marks determine the performance category.
- The first and third examination marks are compared to identify the trend.
- Performance categories are based on the following ranges:
  - 75 and above: Excellent
  - 60–74.99: Good
  - 40–59.99: Average
  - Below 40: Needs Improvement

## 4. Algorithm

1. Start the program.
2. Read the number of students.
3. Create an empty student list.
4. For each student:
   - Read the student's name.
   - Read marks from three examinations.
   - Calculate the average.
   - Classify the performance level.
   - Compare the first and third examination marks.
   - Identify the performance trend.
   - Store the student details.
5. Display the student performance report.
6. Calculate the class average.
7. Display the class summary.
8. Stop the program.

## 5. Flowchart

Start  
↓  
Enter number of students  
↓  
Collect student details  
↓  
Enter three examination marks  
↓  
Calculate average marks  
↓  
Classify performance  
↓  
Compare first and third exam marks  
↓  
Identify performance trend  
↓  
Store student details  
↓  
Display performance report  
↓  
Calculate class average  
↓  
Display class summary  
↓  
End

## 6. Pseudocode

BEGIN

INPUT number_of_students

CREATE empty students list

FOR each student

    INPUT student_name

    INPUT marks for three examinations

    average = SUM(marks) / 3

    IF average >= 75 THEN
        performance = "Excellent"

    ELSE IF average >= 60 THEN
        performance = "Good"

    ELSE IF average >= 40 THEN
        performance = "Average"

    ELSE
        performance = "Needs Improvement"

    END IF

    trend = third_exam_marks - first_exam_marks

    IF trend > 0 THEN
        trend_status = "Improving"

    ELSE IF trend < 0 THEN
        trend_status = "Declining"

    ELSE
        trend_status = "Stable"

    END IF

    STORE student details

END FOR

DISPLAY student performance report

CALCULATE class average

DISPLAY class summary

END

## 7. Python Source Code

The Python program is saved in `performance.py`.

It uses variables, lists, loops, conditional statements, arithmetic operators, and comparison operators to analyse student performance.

## 8. Test Cases

| Test Case | Student | Exam 1 | Exam 2 | Exam 3 | Expected Trend |
|---|---|---:|---:|---:|---|
| TC01 | Ravi | 60 | 70 | 85 | Improving |
| TC02 | Priya | 90 | 85 | 80 | Declining |
| TC03 | Arun | 45 | 50 | 60 | Improving |
| TC04 | Sneha | 80 | 65 | 50 | Declining |
| TC05 | Kiran | 70 | 70 | 70 | Stable |

## 9. Output Screenshots

Add screenshots of the successfully executed Python program in the `screenshots` folder.

## 10. Conclusion

The Student Performance Trend Analysis program successfully evaluates students' academic performance using examination marks. It calculates averages, classifies performance levels, identifies trends, and calculates the class average. This project demonstrates the practical use of Python lists, loops, conditional statements, and operators.