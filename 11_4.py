import pandas as pd

#words = [["Bread", "Butter"], ["Robert", "Larping"]]

#result = pd.DataFrame(words)

#print(result)

student_info = {
    "Name": ["Tom", "LeBron", "George", "LaFawnda"],
    "GPA": [2.7, 4.0, 1.1, 3.6]
}

result = pd.DataFrame(student_info)

print(result)
#print(student_info)

#df = pd.DataFrame([student_info])

#print(df)