num_list = []

for i in range(10):
    num_list.append(int(input(f"Enter any number {i + 1}: ")))

print("Sum of the 10 inputs is:", sum(num_list))