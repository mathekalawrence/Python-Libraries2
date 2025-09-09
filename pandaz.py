#importing pandas
import pandas as pd
#Create a table from a dictionary
data = { 'Name': ['Larry', 'Muia', 'Matheka'],
        'Age': ['67, 23, 43'],
        'City': ['Chicago', 'Berlin', 'Pretoria']
        }
df = pd.DataFrame(data)
print(df)

#new data
df['Salary'] = [2000, 67000, 34000]
print(df)

#Read the CSV file into the dataframe
print()