# es.py
# Shakespeare texts sourced from ProjectGutenberg - https://www.gutenberg.org/ebooks/2267
# Followed instructions from https://www.geeksforgeeks.org/count-the-number-of-times-a-letter-appears-in-a-text-file-in-python/ to assist with completing this task. 
# The menu was like something I built previously in work for a command line menu to select which files to pull down from a company HR website. 
# Author: Paul Callaghan 

import os

def print_menu():
    print("Please select a Shakespearean play by inputting the corresponding number:")
    print("1. Othello")
    print("2. King Lear")
    print("3. Hamlet")
    print("4. The Merchant of Venice")
    print("5. The Taming of the Shrew")
    print("6. The Tempest")
    print("7. As You Like It")
    print("8: Exit Menu")
    return input("Enter your choice: ")

def count_letter_e(file_path, letter):
    with open(file_path, 'r', encoding="utf8") as file:
        contents = file.read()
        return len(contents)
    

file_names = {
    "1": "Othello.txt",
    "2": "KingLear.txt",
    "3": "Hamlet.txt",
    "4": "TheMerchantOfVenice.txt",
    "5": "TheTamingoftheShrew.txt",
    "6": "TheTempest.txt",
    "7": "AsYouLikeIt.txt"
}

while True:
    choice = print_menu()

    if choice == '8':
        print("'A word or two before you go. I have done the state some service, and they know't.' -Othello")
        break
    
    if choice in file_names:
        file_path = file_names[choice]
        if os.path.isfile(file_path):
            letter_count = count_letter_e(file_path, 'e')
            print(f"The letter 'e' appears {letter_count} times in {file_path}.")
        else:
            print("File not found.")
    else:
        print("Invalid selection")

