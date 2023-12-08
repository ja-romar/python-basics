#We can append new line as follows:

with open('Example2.txt', 'a') as testwritefile:
    testwritefile.write("this is other line \n")
    testwritefile.write("this is an other line \n")
    testwritefile.write("and this is other line \n")

#for verify the file has changed running the following code

with open('Example2.txt', 'r') as textwritefile:
    print(testwritefile.read())

