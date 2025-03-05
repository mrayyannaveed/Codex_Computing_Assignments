num_list = [2,4,6,5,3,8,2,6,6,4]

print("Before deletion:", num_list)

for num in num_list:
    if num < 4:
        del num_list[num]
    
print("Number list after deletion is:", num_list)