user_weight = input("Enter your weight: ")
user_height = input("Enter your height: ")

if user_height.isalpha() or user_weight.isalpha():
    print("Invalid Input")
    exit()

bmi = float(user_weight) / float(user_height) ** 2

if bmi < 18.5:
    print(f"Your BMI is {bmi}, You are underweight")
elif 18.5 <= bmi < 24.9:
    print(f"Your BMI is {bmi}, You are normal")
elif 25 <= bmi < 29.9:
    print(f"Your BMI is {bmi}, You are overweight")
elif bmi > 30:
    print(f"Your BMI is {bmi}, You are obese")