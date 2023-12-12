import pandas as pd 

df = pd.DataFrame([
    {'drink': 'soda', 'carbonated?': True, 'temperature': 'cold', 'sugar(tsp)': 10.5, 'calories': 150},

{'drink': 'coffee', 'carbonated?': False, 'temperature': 'hot', 'sugar(tsp)': 3, 'calories': 31},

{'drink': 'smoothie', 'carbonated?': False, 'temperature': 'cold', 'sugar(tsp)': 6, 'calories': 85},

{'drink': 'water', 'carbonated?': False, 'temperature': 'cold', 'sugar(tsp)': 0, 'calories': 0},

{'drink': 'tea', 'carbonated?': False, 'temperature': 'hot', 'sugar(tsp)': 2, 'calories': 43},

{'drink': 'lemonade', 'carbonated?': False, 'temperature': 'cold', 'sugar(tsp)': 9.5, 'calories': 125},

{'drink': 'slushy', 'carbonated?': False, 'temperature': 'cold', 'sugar(tsp)': 8, 'calories': 99},

])

#To set the row lebel indexes to the drink column:

df.set_index('drink', inplace = True)

#print(df)

#print('print with loc method\n',df.loc['tea'])

#print('print with iloc method\n',df.iloc[4])

#To create a DataFrame with a single row 
#print('print Data Frame with loc', df.loc[['tea']])

#print('print Data Frame with iloc', df.iloc[['1']])


#Selects multiple rows of data using a list

aLoc = df.loc[['smoothie', 'tea', 'soda']]
aIloc = df.iloc[[2,4,5]]

#print(aLoc)
#print(aIloc)

#Select multiple rows of data with slicing
#with loc
# IMPORTANT with loc method the start and end parameter are included in the output
locSlicing = df.loc['coffee':'water']

print(locSlicing)

#with iloc, IMPORTANT with this method the start and end parameter are excluded in the output
iloSlicing = df.iloc[0:3]

print(iloSlicing)

#Select a single value from a cell
#With loc
singleLoc = df.loc['coffee','temperature']

print(singleLoc) #this code prints 'hot'

#with Iloc
singleIloc = df.iloc[1,1]

print(singleIloc)#this code prints 'hot'

#Selecting multiple cells Values using a list

multipleLoc = df.loc[['water','lemonade'],['sugar(tsp)','calories']]

print(multipleLoc)

#With iloc

multipleIloc = df.iloc[[1,0], [2.3]]
print(multipleIloc)

#Using a multiple cells values with slice

#With loc
multipleSlice = df.loc[:'water','carbonated?':'sugar(tsp)']
print(multipleSlice)

#With iloc
multipleIloc = df.iloc[3:7, 2:]
print(multipleIloc)

