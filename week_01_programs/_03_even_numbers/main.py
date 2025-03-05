num_list = [2,4,6,5,3,8,2,6,6,4]

index = 0

for evem_num in num_list:
    if evem_num % 2 == 0:
        print(evem_num)
        index += 1

print("Number of even numbers: ", index)