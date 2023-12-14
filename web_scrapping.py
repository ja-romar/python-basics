from bs4 import BeautifulSoup
import requests

html="<!DOCTYPE html><html><head><title>Page Title</title></head><body><h3><b id='boldest'>Lebron James</b></h3><p> Salary: $ 92,000,000 </p><h3> Stephen Curry</h3><p> Salary: $85,000, 000 </p><h3> Kevin Durant </h3><p> Salary: $73,200, 000</p></body></html>"

soup = BeautifulSoup(html,'html5lib')

#to display html in nested structure
print(soup.prettify())
#dislay  title
tag_object = soup.title
print('tag object:',tag_object)

#see the tag type
print("tag object type:",type(tag_object))

tag_object=soup.h3

#the tag object is a tree of objects. we can access the child of the tag or 
#navigate down the branch...
tag_child =tag_object.b
print(tag_child)

#also we access the parent with the parent
parent_tag =tag_child.parent
print(parent_tag)

tag_object.parent

#acces to sibling
sibling_1=tag_object.next_sibling
print(sibling_1)

#access to sibling 2
sibling_2=sibling_1.next_sibling
print(sibling_2)
#print the salary of stepehen curry 
ScurrySalary = sibling_2.next_sibling
print(ScurrySalary)