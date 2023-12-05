# We can write a file .txt

with open('Example2.txt', 'w') as writefile:
    writefile.write("Overwrite\n") #We write in the file Example2.txt


with open('Example2.txt', 'r') as testwritefile:
    print(testwritefile.read()) #we read the content of the file
