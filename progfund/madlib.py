'''PSUEDOCODE
    1. Import os and random
    2. Clear the terminal screen
    3. Declare all variables, use adjectives as list for random
    4. Prompt user for variable input
    5. Clear screen
    6. Print Story
'''

import random
import os
import time
os.system('cls')

adj = input("Enter 4 adjectives, and separate each entry by a space: ")
print("\n")
user_listadj = adj.split()
person = input("Enter the name of a famous person: ")
print("\n")
noun1 = input("Enter a noun(object): ")
print("\n")
noun2 = input("Enter another noun(object): ")
print("\n")
pnoun = input("Enter a plural noun: ")
print("\n")
noun3 = input("Enter a noun (object used for cooking): ")
print("\n")
number = input("Enter a number: ")
print("\n")
shape = input("Enter a plural shape: ")
print("\n")
food1 = input("Enter a food you don't like: ")
print("\n")
food2 = input("Enter a food you really like: ")
print("\n")
number1 = input("Enter a number between 2 and 100: ")

os.system('cls')

print("Pizza was invented by a {} " .format(random.choice(user_listadj))  + "chef named " + person + ".")
print("To make a pizza, you need to take a lump of {} ".format(noun1) + "and make a thin, round {} " .format(random.choice(user_listadj)) + noun2 + ".")
print("Then you cover it with {} " .format(random.choice(user_listadj)) + "sauce, " + "{} " .format(random.choice(user_listadj)) + "cheese, and freshly chopped " + pnoun +".")
print("Next you have to bake it in a very hot " + noun3 + ".")
print("When it is done, cut it into {} " .format(number) + shape + ".")
print("Some people like " + food1 + " pizza the best, but my favorite is the " + food2 + " pizza.")
print("If I could, I would eat pizza " + number1 + " times a day!")