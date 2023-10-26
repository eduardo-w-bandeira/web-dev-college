import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Ted', 'Debra'],
        'salary': [5000, 5200, 7000, 7100],
        'City': ['Vancouver', 'Surrey', 'Burnaby', 'Vancouver']}

df = pd.DataFrame(data)
condition = (df['salary'] < 6000)
filtered_df = df[condition]
result = np.sqrt(filtered_df)

print(df)
