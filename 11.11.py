import pandas as pd

national_park_data = pd.read_csv("national_parks_sample.csv")

#print(national_park_data.loc[national_park_data["Waterfalls"] == "Yes"])

for row, col in national_park_data.iterrows():
    print(row, col)
    print()