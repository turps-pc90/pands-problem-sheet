# es.py
# Othello sourced from ProjectGutenberg - https://www.gutenberg.org/ebooks/2267
# Followed instructions from https://www.geeksforgeeks.org/count-the-number-of-times-a-letter-appears-in-a-text-file-in-python/ to assist with completing this task. 
# Author: Paul Callaghan 

from collections import Counter

#File Path
filePath = r'C:\Users\pcallaghan\HDip\ProgrammingAndScripting\Course Material\Week 7\othello.txt'


file = open(filePath, 'r')

# Store content of the file in a variable
text = file.read()
number_of_characters = len(text)
letter_count = Counter(text)


def letterFrequency(file, letter):
    # open file in read mode
    file = open(filePath, 'r')
 
    # store content of the file in a variable
    text = file.read()
 
    # using count()
    return text.count(letter)
 
 
# call the function and display the letter count
print(letterFrequency(file, 'e'))
