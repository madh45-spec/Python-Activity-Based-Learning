print("==========================================")
print("    INTERNSHIP CANDIDATE RANKING SYSTEM")
print("==========================================")

n = int(input("\nEnter number of candidates: "))

candidates = []

# Collect candidate details
for i in range(n):

    print("\nEnter details of Candidate", i + 1)

    name = input("Enter candidate name: ")

    marks = float(input("Enter academic percentage: "))
    aptitude = float(input("Enter aptitude score (0-100): "))
    interview = float(input("Enter interview score (0-100): "))

    # Calculate overall score
    overall = (marks * 0.40) + (aptitude * 0.30) + (interview * 0.30)

    # Classify candidate
    if overall >= 80:
        result = "Highly Recommended"

    elif overall >= 60:
        result = "Recommended"

    else:
        result = "Not Recommended"

    candidates.append([name, marks, aptitude, interview, overall, result])


# Rank candidates by overall score
candidates.sort(key=lambda candidate: candidate[4], reverse=True)


# Display candidate ranking
print("\n========== INTERNSHIP RANKING ==========")

for i in range(len(candidates)):

    candidate = candidates[i]

    print("\nRank:", i + 1)
    print("Candidate Name:", candidate[0])
    print("Academic Percentage:", candidate[1])
    print("Aptitude Score:", candidate[2])
    print("Interview Score:", candidate[3])
    print("Overall Score:", round(candidate[4], 2))
    print("Selection Status:", candidate[5])


# Display summary
print("\n========== SELECTION SUMMARY ==========")

recommended = 0
not_recommended = 0

for candidate in candidates:

    if candidate[5] == "Highly Recommended" or candidate[5] == "Recommended":
        recommended += 1

    else:
        not_recommended += 1


print("Total Candidates:", len(candidates))
print("Recommended Candidates:", recommended)
print("Not Recommended Candidates:", not_recommended)

print("\n==========================================")
print("       RANKING COMPLETED")
print("==========================================")