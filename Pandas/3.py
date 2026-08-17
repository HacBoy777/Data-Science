import pandas as pd
data = {"Calories": [420,520,620,725,827,924],
        "Duration": [50,60,70,85,95,105]}
df = pd.DataFrame(data,index = ['day 1', 'day 2', 'day 3', 'day 4', 'day 5', 'day 6'])
# df = pd.DataFrame(data)
print(df.loc[['day 1', 'day 3', 'day 5']])