maths_marks = int(input("Enter the marks of maths: "))
chemistry_marks = int(input("Enter the marks of chemistry: "))
physics_marks = int(input("Enter the marks of physics: "))

if int(maths_marks) < 0 or int(maths_marks) > 100 or int(chemistry_marks) < 0 or int(chemistry_marks) > 100 or int(physics_marks) < 0 or int(physics_marks) > 100:
    print("Invalid marks, Enter less than 101")
    exit()

std_marks = {"Maths": maths_marks, "Chemistry": chemistry_marks, "Physics": physics_marks}

for marks in std_marks.values():
    marks += int(marks)
    avg_marks = int(marks) / len(std_marks)
    percentage = (int(marks) / 300) * 100

print(f"""Total Marks of the student: {marks}
Average Marks: {round(avg_marks, 2)}
Percentage: {round(percentage, 2)}""")
    
