import pandas as pd
import numpy as np

# Create a DataFrame
data = {'A': [1, 2, 3, 4, 5], 'B': [10, 20, 30, 40, 50]}
df = pd.DataFrame(data)

# Filter rows based on a NumPy condition
condition = (df['A'] > 2)
filtered_df = df[condition]
print('--- Original Dataframe ---')
print(df)
print('--- Filtered dataframe ----')
print(filtered_df)

# Merge
print('--- Merged dataframe ----')
merged_df = pd.concat([df, filtered_df])
print(merged_df)
