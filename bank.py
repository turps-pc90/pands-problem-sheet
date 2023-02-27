# bank.py
# This program requests the user to input two separate coin amounts and calculates how much that equates to when combined. 
# Author: Paul Callaghan 
import decimal
import math

first_coins = input("How much money (in cent) are you depositing first? - ")
second_coins = input("How much money (in cent) are you depositing second? - ")

total1 = int(first_coins) / 100
total2 = int(second_coins) / 100 

rounded_total1 = decimal.Decimal(total1).quantize(decimal.Decimal('0.00'))
rounded_total2 = decimal.Decimal(total2).quantize(decimal.Decimal('0.00'))

balance = rounded_total1 + rounded_total2
if balance > 1:
    print(f"Your balance is €{balance}. Don't spend it all in one shop.")
else: 
    print(f"Your balance is €{balance}. It won't even get you a bag of crisps these days.")

#Reference
#https://www.tutorialspoint.com/How-to-round-down-to-2-decimals-a-float-using-Python#:~:text=Use%20the%20ceil()%20function,and%20print%20the%20resultant%20number.