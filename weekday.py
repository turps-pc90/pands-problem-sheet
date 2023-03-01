# bank.py
# This program indicates to the user whether it is a weekday or not. 
# Author: Paul Callaghan 
import datetime

day_num = datetime.datetime.today().weekday()

if day_num <= 5:
    print("Today is a weekday")
else:
    print("Weekend, woop woop!")


#Reference
#https://stackoverflow.com/a/29384769/20182382 helped me solve this. 