import pandas as pd #First, we import pandas as pd

#We assign the excel to a df
df = pd.read_excel('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/jupyterlite/files/Module%205/data/TopSellingAlbums.xlsx')

#View data of of a DataFrame with panda

x = df[['Length']]
print(x)

#Also we can view more column data, in this example we acces to a comulm called Artist

artistColumn = df[['Artist']]
print(artistColumn)

#We can acess to a multiple columns at the same time...

multColumns = df[['Artist','Length','Genre']]
print(multColumns)

#We can use the iloc method for acces to a first column and first row...
b = df.iloc[0,0]
print(b)

#For access to a second row and the first column....

c = df.iloc[1,0]
print(c)

