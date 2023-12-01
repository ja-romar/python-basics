#Create a code that allows analyze text.

#Task 1 String in lower case, converte the text in lower case
#Task 2 Return the frequency of all the words in a given string
#Task 3 Return the frequency of an specific word.

#Define a string 
secondgivenstring = "Python es un lenguaje de programación de alto nivel, fácil de aprender y potente. Python se utiliza en una amplia variedad de aplicaciones, desde desarrollo web hasta inteligencia artificial. Una de las ventajas de Python es su sintaxis clara y legible. Esto facilita la escritura y mantenimiento del código. Además, Python cuenta con una gran cantidad de bibliotecas y módulos que hacen que sea versátil y adecuado para diferentes tareas. Python es conocido por su filosofía de baterías incluidas, lo que significa que viene con un conjunto completo de herramientas y módulos estándar. Esto hace que sea fácil comenzar a programar sin tener que instalar muchas cosas adicionales.En resumen, Python es un lenguaje poderoso y flexible que se adapta a diversas necesidades de desarrollo. Si estás interesado en la programación, Python es una excelente opción para comenzar, python."
givenstring = "Lorem ipsum dolor! diam amet, consetetur Lorem magna. sed diam nonumy eirmod tempor. diam et labore? et diam magna. et diam amet."

#Define the class and its attributes
#Implement the promat text in Lowercase:
class TextAnalyzer(object): #The class has beeen created.
    def __init__(self, text):
        # Remove punctation
        # we use remove() method to eliminate punctuation of the string.
        formattedText = text.replace('.','').replace('!','').replace('?','').replace('.','')
        #Now, we make text lower casse
        # We use the method lowercase() to lower the string text.
        formattedText = formattedText.lower()

        #We assign the formatted text to a new attribute of the class

        self.fmtText = formattedText

    #Now is time to implement the code to count the frequency of all unique words.
    def freqAll(self):
        #split text into words
        #we use the method split() with the next sintaxys split(' ')
        wordList = self.fmtText.split(' ')

        #now we create a dictionary
        freqMap = {}
        #now we iterate to remove duplicates in list
        for word in set(wordList):
            freqMap[word] = wordList.count(word)

        return freqMap
    
    #Now we should implement a code to count the freuqency of a specific word:

    def freqOf(self,word): #Define a method that allows coun the word specific frequency
        #get frequency map
        freqDict = self.freqAll()

        if word in freqDict:
            return freqDict[word]
        else:
            return 0
        
        #At this point we have created a class with 3 methods.
        #class called text analyzer
        #methods called lowe case
        #freqAll
        #freqOf

# lets do to try the class that we created.
# Create an instance

analyzed = TextAnalyzer(givenstring)

# Call the function to convert in lower case.
print("Formatted text to lower case:", analyzed.fmtText)

# Now, call the function that count the frequency of all words
freqMap = analyzed.freqAll()
print(freqMap)

#Now is time create a function that count the frequency of a specific word.

word = "lorem"
freqOf = analyzed.freqOf(word)
print(freqOf)

#now its time to try with other text

#create a second instance
analyzed = TextAnalyzer(secondgivenstring)

#Call the funcction to convert all text in lower case.
print("Formatted text to lower case:", analyzed.fmtText)

# Now, call the function that count the frequency of all words.
freqMap = analyzed.freqAll()
print(freqMap)

#Now call the function that count the frequency of a specific word.

word = "python"
freqOf = analyzed.freqOf(word)
print(freqOf)


