import numpy as np #To import and use numpy.

#Create an Numpy Array
a = np.array([0,1,2,3,4]) 
 
print(a)
print(type(a)) #Check the type of the Numpy Array

print(a.dtype) #Check the type of the value on the Numpy Array

#Lets go to create a new Numpy Array
c = np.array([12,11,14,15,16,17])
print('\n\narray with mistake ', c)

#We can change the values on the array with the index.
#In the array we have numbers from 12 to 17 consecutevily, but we have an error, in the element 2 (1 of index)
#Lets to fix it
c[1] = 13
print('\nArrawy without the mistake ', c)

#Also we can use slicing with Numpy Arrays 
d = c[1:4]
print('\nslicing elements' , d)
#this returns [13 14 15]
#Its important to realize that the element at the end '4' not being included in the output

#We can assign new values with slicing...

c[1:4] = [18,19,20]
print('\nvalues change with slicing', c)
#This prints [12 18 19 20 16 17]


###################################################

# We can also define the steps in slicing.


#We create a new array

arr = np.array([1,2,3,4,5,6,7])

print(arr[1:5:2]) #this returns 2 and 4

#if we dont define a start, the start it's 0
print(arr[:4])

#If we dont define a end, the end is the last element of the array.
print(arr[2:])

#If we dont pass step its considered 1
print(arr[0:4])

#Let's to print the even number in on array
evenArr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

print(evenArr[1:8:2])