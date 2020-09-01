#!/usr/bin/env python3

import string
import sys
import re 

textName = sys.argv[1] #Name of the file to read
outPut = sys.argv[2] #Name of the output file 

text = open(textName, 'r') #Open the file in read mode 
dictonary = dict() #Create a new dictonary

for line in text:
    if not line.isspace(): #Check if the line is not empty
        line = re.sub(r"[,.;@?!&$'-]+\ *", " ", line) #Get rid of all punctuation in the line and turn it into a white space
        line = line.strip() #Get rid of leading or traling empty space
        line = line.lower() #Trun all characters into lower case
        words = line.split(" ") #Split the string into tokes by empty spaces
        for word in words: #Traverse all the words in each line
            if word in dictonary: #check if the word is already in the dictonary
                dictonary[word] = dictonary[word] + 1 #If yes add one to the value
            else:
                dictonary[word] = 1 #Else add and give it value 1

orderDictonary = sorted(dictonary) #Order dictonary in alphabetical order

for k in orderDictonary:
    print(k + " " + str(dictonary[k])) #Print dictonary content (debug Tester)