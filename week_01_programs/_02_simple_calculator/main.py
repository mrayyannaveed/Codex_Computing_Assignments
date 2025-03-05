num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

if num1.isalpha() or num2.isalpha():
  print("Invalid input")
  exit()


print("""Select any operation you want to perform
1. Addition(+)
2. Subtraction(-)
3. Multiplication(*)
4. Division(/)""")

calculating = True

while calculating:
  option = input("Enter (1/4) to perform operation: ")

  if not option.isnumeric():
    print("Invalid Input, Enter number between 1-4")
    continue

  if int(option) == 1:
    print(f"Your answer is {round(float(num1) + float(num2), 2)}")
  elif int(option) == 2:
    print(f"Your answer is {round(float(num1) - float(num2), 2)}")
  elif int(option) == 3:
    print(f"Your answer is {round(float(num1) * float(num2), 2)}")
  elif int(option) == 4:
    print(f"Your answer is {round(float(num1) / float(num2), 2)}")
  else:
    print("Invalid input, Enter number between 1-4")

  user_input = input("Enter (y/n): ").lower()

  if not user_input == "y":
    calculating = False

print("Calculation Ends")