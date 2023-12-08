
#This code returns the value most repeated.


x = [1, 2, 3, 4, 5, 6, 7, 1, 2, 1, 2, 1]

most = max(set(x), key=x.count)

print(most)

gretting = ['hello', 'hello', 'hi', 'hola']

mostgrettings =max(set(gretting), key=gretting.count)

print(mostgrettings)