# Case Study 5: Student Timetable Conflict Detection

## 1. Problem Statement

Students attend multiple classes throughout the week. Sometimes two or more classes may be scheduled at overlapping times on the same day. This Python program analyses class schedules and identifies timetable conflicts to help students maintain an organised timetable.

## 2. Objectives

- To collect subject names and class timings.
- To identify overlapping class schedules.
- To compare class timings on the same day.
- To generate a timetable conflict report.
- To display the total number of conflicts.

## 3. Assumptions

- Class timings are entered using the 24-hour format.
- Starting and ending times are entered as whole numbers.
- Class end time must be greater than start time.
- Two classes conflict only when they occur on the same day and their timings overlap.
- Classes starting exactly when another class ends are not considered conflicts.

## 4. Algorithm

1. Start the program.
2. Read the number of classes.
3. Create an empty timetable list.
4. For each class:
   - Read subject name.
   - Read the day.
   - Read starting and ending hours.
   - Validate the entered time.
   - Store valid class details.
5. Compare every pair of classes.
6. Check whether both classes occur on the same day.
7. Check whether their timings overlap.
8. Display detected conflicts.
9. Display the total number of classes and conflicts.
10. Stop the program.

## 5. Flowchart

Start  
↓  
Enter number of classes  
↓  
Collect class details  
↓  
Validate class timings  
↓  
Store valid classes  
↓  
Compare pairs of classes  
↓  
Are classes on the same day?  
↓  
Do their timings overlap?  
- Yes → Display conflict
- No → Continue comparison

↓  
Calculate total conflicts  
↓  
Display timetable summary  
↓  
End

## 6. Pseudocode

BEGIN

INPUT number_of_classes

CREATE empty classes list

FOR each class

    INPUT subject_name
    INPUT day
    INPUT start_time
    INPUT end_time

    IF start_time < 0 OR end_time > 23 OR start_time >= end_time THEN
        DISPLAY "Invalid time"

    ELSE
        ADD class details to classes list

    END IF

END FOR

SET conflicts = 0

FOR i FROM 0 TO length(classes) - 1

    FOR j FROM i + 1 TO length(classes) - 1

        IF classes[i].day = classes[j].day THEN

            IF classes[i].start < classes[j].end
            AND classes[j].start < classes[i].end THEN

                DISPLAY "Conflict Detected"

                conflicts = conflicts + 1

            END IF

        END IF

    END FOR

END FOR

DISPLAY total classes
DISPLAY total conflicts

END

## 7. Python Source Code

The Python program is saved in `timetable.py`.

It uses variables, lists, nested loops, conditional statements, comparison operators, and logical operators to identify overlapping class schedules.

## 8. Test Cases

| Test Case | Subject 1 | Subject 2 | Day | Expected Result |
|---|---|---|---|---|
| TC01 | Mathematics (9–11) | Physics (10–12) | Monday | Conflict |
| TC02 | Chemistry (9–10) | English (10–11) | Tuesday | No Conflict |
| TC03 | Biology (9–10) | Computer Science (11–12) | Wednesday | No Conflict |
| TC04 | History (10–12) | Geography (10–11) | Thursday | Conflict |

## 9. Output Screenshots

Add screenshots of the successfully executed Python program in the `screenshots` folder.

## 10. Conclusion

The Student Timetable Conflict Detection program successfully identifies overlapping class schedules by comparing their days and timings. It helps students organise their academic schedules and avoid timetable clashes. This project demonstrates the practical application of Python lists, nested loops, conditional statements, and logical operators.