def plus(number1, number2):
    return number1 + number2

def minus(number1, number2):
    return number1 - number2

def umnozhenie(number1, number2):
    return number1 * number2

def podelit(number1, number2):
    if number2 == 0:
        print("Zero Division Error !!!")
        return None
    return number1 / number2    

print("Welcome to the Calculator Program!")

try:
    number1 = int(input("Please enter the first number: "))
    number2 = int(input("Please enter the second number: "))

    operation = int(input("""Please select an operation:
        
        1. Addition
        2. Subtraction
        3. Multiplication
        4. Division


    Enter your choice (1-4): """))

    if operation == 1:
        print("The result of addition is: ", plus(number1, number2))

    elif operation == 2:
        print("The result of subtraction is: ", minus(number1, number2))

    elif operation == 3:
        print("The result of multiplication is: ", umnozhenie(number1, number2))

    elif operation == 4:
        result = podelit(number1, number2)
        if result is not None:
            print("The result of division is: ", result)
    else:
        print("Operation was selected incorrectly !!! Your choice must be 1-4 ")       

except ValueError:
    print("Not a number !!! Restart the program and input only numbers.")
