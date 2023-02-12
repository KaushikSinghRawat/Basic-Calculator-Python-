#Addition Function
def add():
    return (a + b)

#Subtraction Function
def subtract():
    return (a - b)

#Multiplication Function
def multiply():
    if a == 0:
        return ('Cannot multiply by "0"')
    elif b == 0:
        return ('Cannot multiply by "0"')
    else:
        return (a * b)

#Division Function
def divide():
    if a == 0:
        return ("0")
    elif b == 0:
        return ("0")
    else:
        return (a / b)

#Percentage Function
def percent():
    return (str((divide()) * 100) + '%')

#Creating Input for the Operators and Operation
a = int(input('Enter 1st operator: '))
b = int(input('Enter 2nd operator: '))
op = input("Enter +, -, *, /, %: ")

#Function for executing operators and operations
def main ():
    if op == '+':
        print (str(add()))
    elif op == '-':
        print (str(subtract()))
    elif op == '*':
        print (str(multiply()))
    elif op == '/':
        print (str(divide()))
    elif op == '%':
        print (STR(percent()))
    else:
        print ('Invalid, please try again')

#Execution of Calculator
main()
