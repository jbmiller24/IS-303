numbers = [2, 1, 2, 5, 6, 5, 7]

unique_list = []

for i in range(len(numbers)):

    is_unique = True

    for j in range(len(numbers)):
        if i != j and numbers[i] == numbers[j]:
            is_unique = False

    if is_unique == True:
        unique_list.append(numbers[i])

print(f"The unique numbers are: {unique_list}")