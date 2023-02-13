while True:
    acc_num = input("Enter your account number: ")
    if len(acc_num) >=4:
        break
    else:
        #Assuming that an account number must be a minimum of 8 characters due to current banking convention
        print("Your account number should be a minimum of 8 characters")



#The safe_acc variable was informed by this Stack Overflow question - https://stackoverflow.com/questions/40842451/how-do-i-use-the-replace-function-to-change-all-but-the-last-4-characters-of
safe_acc = 'X'*(len(acc_num) - 4)+acc_num[-4:]
print(f'Your account number is {safe_acc}')
