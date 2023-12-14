from bs4 import BeautifulSoup
import requests

table="<table><tr><td id='flight'>Flight No</td><td>Launch site</td> <td>Payload mass</td></tr><tr> <td>1</td><td><a href='https://en.wikipedia.org/wiki/Florida'>Florida<a></td><td>300 kg</td></tr><tr><td>2</td><td><a href='https://en.wikipedia.org/wiki/Texas'>Texas</a></td><td>94 kg</td></tr><tr><td>3</td><td><a href='https://en.wikipedia.org/wiki/Florida'>Florida<a> </td><td>80 kg</td></tr></table>"

table_bs = BeautifulSoup(table, 'html5lib')

#find_all method
#find looks throug a tag's descendants and retrieves all desendants that match

#name
table_rows = table_bs.find_all('tr')
print(table_rows)

first_row = table_rows[0]
print(first_row)

#We can obtain the child
print(first_row.td)

#iterate the list 
for i, row in enumerate(table_rows):
    print('row',i,'is',row)
#iterate and obtain rows an colums
for i,row in enumerate(table_rows):
    print("row",i)
    cells=row.find_all('td')
    for j,cell in enumerate(cells):
        print('colunm',j,"cell",cell)

list_input = table_bs.find_all(name=["tar", "td"])
print(list_input)

#We can filter with the id attribute
#filter based on a Id value 

table_bs.find_all(id="flight")

#We can find all the elements that have llinks for example to the florida wikipedia page

list_input=table_bs.find_all(href="https://en.wikipedia.org/wiki/Florida")
print(list_input)

#find a href attribute
table_bs.find_all(href=True)

#find strings 
looked = table_bs.find_all(string="Florida")
print(looked)