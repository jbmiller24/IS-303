import pandas as pd

park_info = pd.read_csv("national_parks_sample.csv")

#parkloc = park_info.loc[park_info["StateOrStates"] == "Utah"]

#parkiloc = park_info.iloc[park_info["StateOrStates"] == "Utah"]

#parkiloc = park_info.iloc[4]

#print(parkloc)
#print(parkiloc)

#query1 = park_info.loc[(park_info["Region"] == "Southeast") &
    #(park_info["CampingAvailable"] == "Yes"),
    #["Park", "StateOrStates", "AnnualVisitorsThousands", "TrailMiles"]]

#print(query1)

query2 = park_info.query('Park == "Everglades"')[["Park", "Region", "TrailMiles"]]


print(query2)