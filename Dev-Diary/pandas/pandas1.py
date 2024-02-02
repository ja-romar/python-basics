import pandas as pd 


# Creating a DataFrame from a dictionary
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 28],
        'City': ['Monterrey', 'Chihuahua', 'CDMX', 'Sonora']}

df = pd.DataFrame(data)

print(df)

