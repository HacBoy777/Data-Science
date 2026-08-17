# Print forst 3 and last 2 records and show only name and city columns find avg age, find records where age is greater then 20
import pandas as pd
data = {'Name': ['John', 'Anna', 'Peter', 'Linda', 'James', 'Laura'],
        'Age': [28, 24, 35, 32, 30, 29],
        'City': ['New York', 'Paris', 'Berlin', 'London', 'Tokyo', 'Sydney'],
        'Score': [85,92,88,76,95,99]}
df = pd.DataFrame(data)
# print("First 2:",df.head(3))
# print("Last 2:",df.tail(2))
# print("Name and City columns:")
# print(df[['Name','City']])
# # print("Average Age:",df['Age'].mean())
# print("Age greater than 20:")
# print(df[df['Age'] > 20])
# print(df[df['City'].isin(['New York','London'])])
# print(df.sort_values("Age"))
# print(df.sort_values("Score",ascending=False))
df["Passed"] = df["Score"] > 80
print(df)