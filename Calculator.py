# Create a basic calculator program using Python.
#
# The program should allow the user to perform simple arithmetic operations on two numbers.
#
# Requirements:
#
# Prompt the user to enter two numbers.
# Prompt the user to select an operation from the following options:
# addition
# subtraction
# multiplication
# division.

print("Welcome to the Calculator Program!")

a = float(input("Please enter the first number:"))
b = float(input("Please enter the second number:"))

def addition(a, b):
    return a + b

def substraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    return a / b

c = int(input("""Please select an operation:
1. Addition
2. Subtraction
3. Multiplication
4. Division 

Enter your choice (1-4): """))

if c == 1:
    print("The result of addition is:", addition(a, b))
elif c == 2:
    print("The result of substraction is:", substraction (a, b))
elif c == 3:
    print("The result of multiplication is:", multiplication (a, b))
elif c == 4 :
    if b == 0 :
        print("Error: Division by zero. Please restart the program and input not 0 second number")
    else:
        print("The result of division is:", division (a, b))
else :
    print("Error: only 1 to 4 must be chosen")
