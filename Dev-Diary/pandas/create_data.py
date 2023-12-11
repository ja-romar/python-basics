import pandas as pd #First, we import pandas as pd

#We assign the excel to a df
df = pd.read_excel('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/jupyterlite/files/Module%205/data/TopSellingAlbums.xlsx')

#View data of of a DataFrame with panda

x = df[['Length']]
print(x)