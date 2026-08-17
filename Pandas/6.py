# What is CSV File ?
# A CSV (COMMA SEPARATED VALUES) file is a text file that has specific format which allow data to be saved in a table structure format.
import pandas as pd 
df = pd.read_csv("Pandas\Dataset\mydata.csv") 
# print(df)
# print(df.to_string())
print(df.loc[0:4])