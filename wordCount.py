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
        line = line.strip() #Get rid of leading or traling empty space
        line = line.lower() #Trun all characters into lower case
        line = re.sub(r"[,.;@?!&$'-]+\ *", " ", line) #Get rid of all punctuation in the line and turn it into a white space
        word = line.split(" ") #Split the string into tokes by empty spaces
    print(line, word) #Print the string and the tokenized vesion (Debug Tester)
