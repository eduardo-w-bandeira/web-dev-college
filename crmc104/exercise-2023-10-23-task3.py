import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Ted', 'Debra'],
        'salary': [5000, 5200, 7000, 7100],
        'City': ['Vancouver', 'Surrey', 'Burnaby', 'Vancouver']}

df = pd.DataFrame(data)
print(df)

# delete ‘Ted’ information from dataframe
print()
df = df.drop(2)

# add new employee with these details: 'Mark', 4500, 'Vancouver’
data_to_add = {'Name': ['Mark'], 'salary': [4500], 'City': ['Vancouver']}
new_employee = pd.DataFrame(data_to_add)
df = pd.concat([df, new_employee], ignore_index=True)
print()
print(df)

# print dataframe for all employees who live in 'Vancouver’.
condition = (df['City'] == "Vancouver")
filtered_df = df[condition]
print()
print(filtered_df)

# print employees names and their salaries.
print()
condition = ['Name', 'salary']
print(df[condition])
