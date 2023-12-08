import pandas as pd 
data = {'Student': ['David', 'Samuel', 'Terry', 'Evan'],
       'Age': [27, 24, 22, 32],
       'Country': ['UK', 'Canada', 'China', 'USA'],
       'Course': ['Python', 'Data Structures', 'Machine Learning', 'Web Development'],
       'Marks': [85, 72, 89, 76]}

df = pd.DataFrame(data)

print(data)
#We retrieves the Marks column and assign it to a variable b
b = df[['Marks']]
b
print(b) #Prints Marks column

#Retrieves the Country and Course columns and assignt it to a variable c

c = df[['Country', 'Course']]
c
print(c)