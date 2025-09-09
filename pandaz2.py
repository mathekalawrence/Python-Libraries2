import pandas as pd
#Create a DataFrame(tabular structure)
data ={
    'Username': ['Muia', 'Larry', 'Kisaa', 'Matheka'],
    'Age': [27, 25, 30, 61],
    'Score': [78, 89, 75, 97]
}

df = pd.DataFrame(data)
print(df)

#Accessing the columns
print("Usernames:", df['Username'])

#Filter rows
print("Scores above 90:")
print(df[df['Score']>90])

df = pd.read_csv('students.csv')
print(df.head()) #Shows first 5 rows