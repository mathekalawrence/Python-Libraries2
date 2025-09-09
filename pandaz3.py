import pandas as pd

#Creating a DataFrame
student={
    'Name':['Mr', 'Mrs', 'Miss'],
    'Age': [78, 46, 26],
    'Gauge': [100, 456, 280]
}

df =pd.DataFrame(student)
