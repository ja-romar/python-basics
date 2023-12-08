#We can write a text file with the write mo

with open('Example2.txt', 'w') as writefile:
    writefile.write("Overwrite\n") #We write in the file Example2.txt
  

with open('Example2.txt', 'r') as testwritefile:
    print(testwritefile.read()) #we read the content of the file


with open('Example2.txt', 'w') as writefile: #this overwrite the line with the text "Overwrite a second line"
    writefile.write("Overwrite a second line\n") #We write in the file Example2.txt
