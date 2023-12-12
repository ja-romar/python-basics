import pandas as pd

#Create a dictionary

data = {
    'Name': ['Robert','Ferran','Lamine','Raphinha','Joao'],
    'Age': [35,23,16,26,23],
    'Country': ['Poland','Spain','Spain','Brazil','Portugal'],
    'Jersey': [9,7,27,11,14]
}

dfBarca = pd.DataFrame(data)

print(dfBarca)  

#Acces to a single player row

player1 = dfBarca.iloc[0] 
print('Robert Lewandowski info \n',player1) #printe the Robert data

#Acces to a country of players (print a collumn with all the values)

country = dfBarca.loc[:,'Country']

print(country)

#Acces to a jersey value of Joao

joaoJersey = dfBarca.iloc[4,3]
print(joaoJersey)