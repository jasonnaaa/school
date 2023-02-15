import math
import os

os.system('cls')

x = int(input("Enter a number for which you want to know the square root of: "))
y = int(input("How many times should we try to improve the guess?: "))

def newton(y):
    a = int(x/2)
    b = math.sqrt(x)
    while y > 0:
        a = (a + (x/a)) / 2
        c = math.fabs(a-b)
        print("A guess is: " + str(a) + " - How close?: " + str(c))
        y = y - 1
        
newton(y)