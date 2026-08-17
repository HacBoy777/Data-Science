import pandas as pd 
data = {
    'Department': ['HR', 'Finance', 'IT', 'HR', 'Sales', 'IT'],
    'Employees': [10, 15, 25, 20, 30, 22],
    'Salary': [50000, 60000, 70000, 55000, 65000, 72000]
}
df = pd.DataFrame(data)
# print(df)
print(df['Salary'])
print(df['Salary'].mean())
print(df.groupby('Department')['Salary'].mean())
print(df[df['Department'] == 'IT']["Salary"].max())