subject_marks = []

for i in range(5):
    subject_marks.append(int(input(f"Enter marks of subject {i + 1}: ")))

for marks in subject_marks:
    if marks > 100:
        print("Invalid marks entered. Marks should be between 0 and 100.")
        continue

    if 50 <= marks <= 100:
        print("You are pass")
    else:
        print("You are fail")
        