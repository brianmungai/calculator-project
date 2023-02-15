number1 = eval(input("enter 1st number"))
number2 = eval(input("enter 2nd number"))

operator = input ("enter operator")
def add (num1, num2):
    result = num1 + num2
    print (result)
def subtract (num1, num2):
    result = num1 - num2
    print (result)
def divide (num1 , num2):
    result = num1 / num2
    print (result)
def multiply (num1,num2):
    result = num1 * num2
    print (result)
if operator == "+":
    add(number1,number2)
elif operator == "-":
    subtract(number1,number2)
elif operator == "/":
    divide(number1,number2)
elif operator == "X" or "x" or "*":
    multiply(number1,number2)
else:
    print("invalid operator")


