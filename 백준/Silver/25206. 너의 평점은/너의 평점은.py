score_sum = 0
total_credit = 0
subject_score = {"A+" : 4.5, "A0" : 4.0, "B+": 3.5, "B0": 3.0, "C+": 2.5, "C0": 2.0, "D+": 1.5, "D0": 1.0, "F": 0.0}

for i in range(20):
    name, credit, score = input().split()
    if score != "P":
        score_sum += float(credit) * subject_score[score]
        total_credit += float(credit)
print(f"{score_sum / total_credit}")