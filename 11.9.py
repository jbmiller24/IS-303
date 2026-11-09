#numbers = [2, 1, 2, 5, 6, 5, 7]

#unique_list = []

#for i in range(len(numbers)):
    #for j in range(i + 1, len(numbers)):
        #if numbers[i] != numbers[j]:
            #unique_list.append(numbers[i])

#print(f"The unique numbers are: {unique_list}")

import pandas as pd

national_park_data = pd.read_csv("national_parks_sample.csv")

print(national_park_data)