# Case Study 9: Multi-Criteria Internship Candidate Ranking

## 1. Problem Statement

Develop a Python program to rank internship candidates based on multiple selection criteria, including academic percentage, aptitude score, and interview performance. The system calculates an overall score for each candidate, classifies their selection status, and generates a merit ranking.

## 2. Objectives

- Collect candidate details and scores.
- Calculate an overall performance score.
- Apply different weightages to selection criteria.
- Classify candidates based on their scores.
- Rank candidates from highest to lowest score.
- Display a selection summary.

## 3. Assumptions

- Academic percentage, aptitude score, and interview score are entered on a scale of 0–100.
- Academic performance carries 40% weightage.
- Aptitude score carries 30% weightage.
- Interview score carries 30% weightage.
- Overall score of 80 or above: Highly Recommended.
- Overall score of 60 or above: Recommended.
- Overall score below 60: Not Recommended.

## 4. Algorithm

1. Start the program.
2. Read the number of candidates.
3. Collect each candidate's name, academic percentage, aptitude score, and interview score.
4. Calculate the overall score using the assigned weightages.
5. Classify each candidate based on the overall score.
6. Store candidate details in a list.
7. Sort candidates in descending order of overall score.
8. Display the ranked candidate list.
9. Calculate the number of recommended and not recommended candidates.
10. Display the selection summary.
11. Stop the program.

## 5. Flowchart

Start  
↓  
Enter Number of Candidates  
↓  
Input Candidate Details  
↓  
Calculate Overall Score  
↓  
Classify Selection Status  
↓  
Store Candidate Details  
↓  
Sort Candidates by Overall Score  
↓  
Display Ranking  
↓  
Calculate Selection Summary  
↓  
Display Results  
↓  
Stop

## 6. Pseudocode

```text
START

INPUT number_of_candidates

CREATE empty candidates list

FOR each candidate

    INPUT name
    INPUT academic_percentage
    INPUT aptitude_score
    INPUT interview_score

    overall_score =
        (academic_percentage * 0.40) +
        (aptitude_score * 0.30) +
        (interview_score * 0.30)

    IF overall_score >= 80
        status = "Highly Recommended"
    ELSE IF overall_score >= 60
        status = "Recommended"
    ELSE
        status = "Not Recommended"
    END IF

    STORE candidate details in candidates list

END FOR

SORT candidates by overall_score in descending order

DISPLAY candidate ranking

COUNT recommended candidates
COUNT not recommended candidates

DISPLAY selection summary

STOP
```

## 7. Python Source Code

**File Name:** `internship.py`

The complete Python implementation is available in this folder. It uses variables, conditional statements, loops, lists, and list sorting to rank candidates.

## 8. Test Cases

| Candidate | Academic % | Aptitude | Interview | Expected Score | Expected Status |
|---|---:|---:|---:|---:|---|
| Ravi | 85 | 90 | 80 | 85.0 | Highly Recommended |
| Priya | 95 | 85 | 90 | 90.5 | Highly Recommended |
| Arun | 60 | 65 | 70 | 64.5 | Recommended |
| Sneha | 75 | 80 | 85 | 79.5 | Recommended |

### Expected Ranking

1. Priya – 90.5
2. Ravi – 85.0
3. Sneha – 79.5
4. Arun – 64.5

## 9. Output Screenshots

The screenshots of the program execution are stored in the `screenshots` folder.

- `output1.png` – Candidate details and ranking.
- `output2.png` – Selection summary.

## 10. Conclusion

The Multi-Criteria Internship Candidate Ranking system successfully evaluates and ranks candidates using multiple selection criteria. It demonstrates the practical application of Python variables, arithmetic operators, conditional statements, loops, lists, and sorting operations. The program helps organize candidate evaluation in a simple and systematic manner.