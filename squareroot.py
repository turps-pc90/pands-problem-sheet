# squareroot.py
# This program calcualtes the square root of an integer by using the Newton Square Root Formula and is based on the article found here - 
#https://tutorialsinhand.com/Articles/python-program-to-find-square-root-of-a-number-using-newton-square-root-formula.aspx#:~:text=If%20a%20given%20number%20is,correct%20square%20root%20of%20N.
# while also learning from  https://stackoverflow.com/questions/55232484/newtons-method-for-approximating-square-roots and  
# https://thirumalai2024.medium.com/python-program-to-find-square-root-of-the-number-using-newtons-method-937c0e732756
# Author: Paul Callaghan 
n = input("Enter a positive number or enter/return to quit: ")

def newtonSqrt(n):     
    n = float(n)
    approx=0.5*n
    better=0.5*(approx+n/approx)
    while better!=approx:
        approx=better
        better=0.5*(approx+n/approx)
    #return approx
    print(better)


if __name__ == '__main__':
    newtonSqrt(n)
    print('Functions called successfully')