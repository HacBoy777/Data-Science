import pandas as pd
data = {'Name': ['John', 'Anna', 'Peter', 'Linda', 'James', 'Laura'],
        'Age': [28, 24, 35, 32, 30, 29],
        'City': ['New York', 'Paris', 'Berlin', 'London', 'Tokyo', 'Sydney'],
        'Score': [85,92,88,76,95,99]}
df = pd.DataFrame(data)
# # print(df)
# print(df.head())
print(df.tail())