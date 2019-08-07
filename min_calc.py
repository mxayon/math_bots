### Mini-Calc Bot
### Operators: a = addition; s = subtraction; m = multiplication; d = division
### User input operator, num1, num2

## adds two inputs
def add(num1, num2):
    return num1 + num2

## subtracts two inputs
def subtract(num1, num2):
    return num1 - num2

## multiplys two inputs
def multiply(num1, num2):
    return num1 * num2

## divides two inputs
def divide(num1, num2):
    return num1 / num2

def calculator():
    # Take input from the user
    operation = input('''
    Type in the math operator you wish Calc Bot to implement..
    + for addition
    - for subtraction
    * for multiplication
    / for division
    ''')

    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    if operation == '+':
        print(num1, "+", num2, "=",
                    add(num1, num2))
    elif operation == '-':
        print(num1, "-", num2, "=",
                    subtract(num1, num2))
    elif operation == '*':
        print(num1, "x", num2, "=",
                    multiply(num1, num2))
    elif operation == 'd':
        print(num1, "/", num2, "=",
                    divide(num1, num2))
    else:
        print("Cannot compute. Please use a for addition, s for subtraction, m for multiplication, or d for division")

    def recalculate():
        recalc = input('''
        Let calc-bot know if you would like me to process numbers again!
        Just use Y for yes and N for no
        ''')
        if recalc == 'Y':
            calculator()
        elif recalc == 'N':
            print('Leaving Mini-Calc Bot.. Come back for more mini functions!')
        else:
            print('Leaving Mini-Calc Bot.. Come back for more mini functions!')
    recalculate()

def welcome():
    print('''
    Hello, I am Calc-bot, here for all your mini math operations and needs.
    ''')

welcome()
calculator()
