# Case Study 10: Smart Campus Incident and Maintenance Prioritization

## 1. Problem Statement

Develop a Python program to manage campus maintenance incidents by evaluating their urgency and impact. The system calculates priority scores, classifies incidents, and generates a ranked maintenance queue to help campus authorities address important issues first.

## 2. Objectives

- Collect campus incident details.
- Evaluate incident urgency and impact.
- Calculate priority scores.
- Classify incidents into priority levels.
- Rank incidents based on priority scores.
- Generate an incident summary.

## 3. Assumptions

- Urgency levels are Low, Medium, High, and Critical.
- Impact levels are Low, Medium, and High.
- Urgency points:
  - Critical = 4
  - High = 3
  - Medium = 2
  - Low = 1
- Impact points:
  - High = 3
  - Medium = 2
  - Low = 1
- Priority Score = (Urgency Points × 2) + Impact Points.
- Score 9 or above = Critical Priority.
- Score 7 or above = High Priority.
- Score 5 or above = Medium Priority.
- Below 5 = Low Priority.

## 4. Algorithm

1. Start the program.
2. Read the number of incidents.
3. Collect incident title and location.
4. Read urgency and impact levels.
5. Assign points based on urgency and impact.
6. Calculate the priority score.
7. Classify the incident priority.
8. Store incident details in a list.
9. Sort incidents in descending order of priority score.
10. Display the ranked maintenance queue.
11. Calculate the number of incidents in each priority category.
12. Display the incident summary.
13. Stop the program.

## 5. Flowchart

Start  
↓  
Enter Number of Incidents  
↓  
Input Incident Details  
↓  
Assign Urgency and Impact Points  
↓  
Calculate Priority Score  
↓  
Classify Priority Level  
↓  
Store Incident Details  
↓  
Sort Incidents by Priority Score  
↓  
Display Maintenance Queue  
↓  
Calculate Priority Summary  
↓  
Display Results  
↓  
Stop

## 6. Pseudocode

```text
START

INPUT number_of_incidents

CREATE empty incidents list

FOR each incident

    INPUT title
    INPUT location
    INPUT urgency
    INPUT impact

    ASSIGN urgency_points
    ASSIGN impact_points

    priority_score =
        (urgency_points * 2) + impact_points

    IF priority_score >= 9
        priority = "Critical Priority"
    ELSE IF priority_score >= 7
        priority = "High Priority"
    ELSE IF priority_score >= 5
        priority = "Medium Priority"
    ELSE
        priority = "Low Priority"
    END IF

    STORE incident details

END FOR

SORT incidents in descending order

DISPLAY maintenance queue

COUNT incidents in each priority category

DISPLAY incident summary

STOP
```

## 7. Python Source Code

**File Name:** `incident.py`

The complete Python implementation is available in this folder. It uses variables, conditional statements, loops, lists, arithmetic operators, and sorting operations.

## 8. Test Cases

| Incident | Urgency | Impact | Expected Score | Expected Priority |
|---|---|---|---:|---|
| Water Leakage | Critical | High | 11 | Critical |
| Computer Lab Network Issue | High | High | 9 | Critical |
| Broken Fan | Medium | Medium | 6 | Medium |
| Library Light Failure | Low | Low | 3 | Low |

### Expected Ranking

1. Water Leakage – 11
2. Computer Lab Network Issue – 9
3. Broken Fan – 6
4. Library Light Failure – 3

## 9. Output Screenshots

The screenshots of the program execution are stored in the `screenshots` folder.

- `output1.png` – Ranked campus maintenance queue.
- `output2.png` – Incident priority summary.

## 10. Conclusion

The Smart Campus Incident and Maintenance Prioritization system successfully evaluates and ranks maintenance incidents based on urgency and impact. It demonstrates the practical application of Python variables, operators, conditional statements, loops, lists, and sorting operations. The system helps organize campus maintenance tasks according to their priority.