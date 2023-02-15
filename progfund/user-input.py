'''
name = input("please tell me your name: ")
age = input("How old are you? ")
print("Nice to meet you, " + name + "! " + "Age: " + age)


num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
result1 = num1 + num2
print(result1)


num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
result1 = int(num1) + int(num2)
print(result1)
'''
#calculator, use of adding floats
num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
result2 = float(num1) + float(num2)
#print(result2)

#formatting for the calculator
print("I see that you have entered {}".format(num1),
"and then added {}".format(num2),
"to get a total of {}".format(result2) + ".",
sep='.\n'
)