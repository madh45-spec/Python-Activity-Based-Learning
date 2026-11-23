print("==========================================")
print("   SMART CAMPUS INCIDENT MANAGEMENT")
print("==========================================")

n = int(input("\nEnter number of incidents: "))

incidents = []

# Collect incident details
for i in range(n):

    print("\nEnter details of Incident", i + 1)

    title = input("Enter incident title: ")
    location = input("Enter incident location: ")

    urgency = input("Enter urgency (Low/Medium/High/Critical): ").lower()
    impact = input("Enter impact (Low/Medium/High): ").lower()

    # Assign urgency points
    if urgency == "critical":
        urgency_points = 4

    elif urgency == "high":
        urgency_points = 3

    elif urgency == "medium":
        urgency_points = 2

    elif urgency == "low":
        urgency_points = 1

    else:
        print("Invalid urgency! Incident skipped.")
        continue

    # Assign impact points
    if impact == "high":
        impact_points = 3

    elif impact == "medium":
        impact_points = 2

    elif impact == "low":
        impact_points = 1

    else:
        print("Invalid impact! Incident skipped.")
        continue

    # Calculate priority score
    score = (urgency_points * 2) + impact_points

    # Classify incident priority
    if score >= 9:
        priority = "Critical Priority"

    elif score >= 7:
        priority = "High Priority"

    elif score >= 5:
        priority = "Medium Priority"

    else:
        priority = "Low Priority"

    incidents.append([title, location, urgency, impact, score, priority])


# Sort incidents by priority score
incidents.sort(key=lambda incident: incident[4], reverse=True)


# Display maintenance priority queue
print("\n========== CAMPUS MAINTENANCE QUEUE ==========")

for i in range(len(incidents)):

    incident = incidents[i]

    print("\nRank:", i + 1)
    print("Incident:", incident[0])
    print("Location:", incident[1])
    print("Urgency:", incident[2])
    print("Impact:", incident[3])
    print("Priority Score:", incident[4])
    print("Priority Level:", incident[5])


# Calculate priority summary
critical = 0
high = 0
medium = 0
low = 0

for incident in incidents:

    if incident[5] == "Critical Priority":
        critical += 1

    elif incident[5] == "High Priority":
        high += 1

    elif incident[5] == "Medium Priority":
        medium += 1

    else:
        low += 1


# Display summary
print("\n========== INCIDENT SUMMARY ==========")

print("Total Incidents:", len(incidents))
print("Critical Priority:", critical)
print("High Priority:", high)
print("Medium Priority:", medium)
print("Low Priority:", low)

print("\n==========================================")
print("       ANALYSIS COMPLETED")
print("==========================================")