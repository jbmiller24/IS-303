import pandas as pd

words = ["Bread", "Butter", "Robert", "Larping"]

result = pd.DataFrame(words)

print(result)

student_info = {
    "name": "Zendaya",
    "year": "Freshman",
    "age": 30,
    "graduated": False,
    "fav_class": "Accounting 310"
}

print(student_info)

df = pd.DataFrame([student_info])

print(df)