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

print("MiniCalc Bot at your service.. Please enter a command -\n"
        "a = add\n" \
        "s = subtract\n" \
        "m = multiply\n" \
        "d = divide\n")

# Take input from the user
select = input("Select operations from a, s, m, d:")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if select == 'a':
    print(num1, "+", num2, "=",
                add(num1, num2))
elif select == 's':
    print(num1, "-", num2, "=",
                subtract(num1, num2))
elif select == 'm':
    print(num1, "x", num2, "=",
                multiply(num1, num2))
elif select == 'd':
    print(num1, "/", num2, "=",
                divide(num1, num2))
else:
    print("Cannot compute. Please use a for addition, s for subtraction, m for multiplication, or d for division")
