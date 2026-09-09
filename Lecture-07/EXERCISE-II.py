
performance_data = {
    "Sales": {
        "Alice": [80, 85, 88, 90],
        "Bob": [70, 75, 78, 80],
        "Charlie": [60, 65, 70, 72]
    },
    "Engineering": {
        "David": [90, 92, 94, 95],
        "Eva": [85, 88, 87, 90],
        "Frank": [88, 87, 86, 85]
    },
    "HR": {
        "Grace": [70, 72, 74, 76],
        "Heidi": [65, 68, 70, 73],
        "Ivan": [60, 62, 64, 66]
    }
}

average_scores = {}
for department, employees in performance_data.items():
    average_scores[department] = {}
    for employee, scores in employees.items():
        average_scores[department][employee] = sum(scores) / len(scores)

# 1. Average Performance Scores
print("Average Performance Scores:", average_scores)

# 2. Top Performers
print("Top Performers:", {department: (max(employees.items(), key=lambda item: item[1])) for department, employees in average_scores.items()})

# 3. Best Department
department_averages = {department: sum(employees.values()) / len(employees) for department, employees in average_scores.items()}
best_department, best_score = max(department_averages.items(), key=lambda item: item[1])
print("Best Department:", best_department, best_score)

# 4. Continuous Improvements
continuous_improvements = {}
for department, employees in performance_data.items():
    continuous_improvements[department] = []
    for employee, scores in employees.items():
        if all(scores[i] < scores[i + 1] for i in range(len(scores) - 1)):
            continuous_improvements[department].append(employee)

print("Continuous Improvements:", continuous_improvements)

# 5. Summary Report
print("\nSummary Report:")
for department, employees in average_scores.items():
    print(f"Department: {department}")
    for employee, average in employees.items():
        print(f"    {employee}: Average Score = {average:.2f}")
    top_employee, top_score = max(employees.items(), key=lambda item: item[1])
    print(f"Top Performer: {top_employee} with Average Score = {top_score:.2f}")

best_department, best_score = max(department_averages.items(), key=lambda item: item[1])
print(f"\nBest Department: {best_department} with Average Score = {best_score:.2f}")