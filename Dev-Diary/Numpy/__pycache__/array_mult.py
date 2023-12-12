import numpy as np

#We create a numpy array

x = np.array([1, 2])
print(x)

#create another array 
y = np.array([2,1])

print(y)

z = np.multiply(x, y)
print(z)

#this operation is equivalent to multiplying by a scaler.

#other example

example = np.array([3,2])
example2 = np.array([2,2])

result = np.multiply(example,example2)
print(result)