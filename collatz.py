# collatz.py
# Week 4 - This program takes user input (a positive int) and outputs successive values. 
# Author: Paul Callaghan 
# Used https://www.sanfoundry.com/python-program-test-collatz-conjecture-given-number/ to inform how to solve this task. 

def collatz(your_num):
    while your_num > 1:
        print(your_num, end=" ")
        if (your_num % 2):
            # your_num is odd
            your_num = (3 * your_num) + 1
        else:
             # your_num is even
             your_num = your_num // 2
    print(1, end = " ")

your_num = int(input("Enter a positive whole number: "))
print("Sequence: ", end="")
collatz(your_num)