# What is DataFrame ??
# A dataframe in pandas is a two dimensional data structure, like two dimensional array or table with rows and columns.
import pandas as pd

# df = pd.DataFrame({'name': ['Alice', 'Bob', 'Charlie'], 
#                    'age': [25, 30, 35],
#                    'gender': ['F', 'M', 'M']},
#                    index=[1, 2, 3])
# print(df)

df = pd.DataFrame({'name': ['Alice', 'Bob', 'Charlie'], 
                   'age': [25, 30, 35],
                   'gender': ['F', 'M', 'M']},
                   index=[1, 2, 3])
print(df.to_string(index = False))
