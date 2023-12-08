import pandas as pd 

#We create a dataframe with a dictionary
data = {'PlayerName': ['Robert', 'Frenkie', 'Marc', 'Joao'],
        'Age': [35, 26, 34, 24],
        'Country': ['Poland', 'Neatherlands', 'Germany', 'Portugal'],
        'Position': ['Forward', 'Midfielder', 'Goalkeeper', 'Forward']}

df = pd.DataFrame(data)




print(df)

#Export the DataFrame file to a CSV file
df.to_csv('output.csv', index=False)

#Export to excel 
df.to_excel('output.xlsx', index=False)