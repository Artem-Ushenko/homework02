# python01-hw % calculator.py
# Welcome to the Calculator Program!

# Please enter the first number: 10
# Please enter the second number: 5

# Please select an operation:
# 1. Addition
# 2. Subtraction
# 3. Multiplication
# 4. Division
#
# Enter your choice (1-4): 3

# The result of multiplication is: 50

print("Welcome to the Calculator Program!")

a = int(input("Please enter the first number:"))
b = int(input("Please enter the second number:"))

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
    print("The result of division is:", division (a, b))
else :
    print("Error: only 1 to 4 must be chosen")
