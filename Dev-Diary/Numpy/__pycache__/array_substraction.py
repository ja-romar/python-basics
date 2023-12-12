import numpy as np

a = np.array([10 ,20, 30])
print(a)

b = np.array([5, 10, 15])
print(b)

#We can substract the two arrays and assign it to c

c = np.subtract(a, b)
print(c)

#Let't do other example

simple = np.array([2,3,4])
otherSimplet = np.array([1,1,1])

result = np.subtract(simple, otherSimplet)
print(result)#Print 1, 2, 3
#in other words rest 1 to each element