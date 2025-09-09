import pandas as pd

#Creating a DataFrame
student={
    'Name':['Mr', 'Mrs', 'Miss'],
    'Age': [78, 46, 26],
    'Gauge': [100, 456, 280]
}

df =pd.DataFrame(student)

print(df)
print()

#Adding a "passed" column where gauge < 200
df['Passed'] = df['gauge']>200
print("DataFrame with Passed Columns")
print(df)