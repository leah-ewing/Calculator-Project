"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code
while True:
    user_input = input("enter your equation ")
    tokens = user_input.split(" ")  
    if "q" in tokens:
        print("Exiting")
        break
    elif len(tokens) < 2:
        print("That's not enough, silly goose!")
        continue
    elif len(tokens) > 3:
        print ("That's too many!")
        continue

    operator = tokens[0]
    num1 = tokens[1]

    if len(tokens) < 3:
        num2 = "0"    
    else:
        num2 = tokens[2]
    
    if len(tokens) > 3:
        num3 = tokens[3]

    result = None

    if not num1.isdigit() or not num2.isdigit():
        print("Those aren't numbers!")
        continue

    if operator == "+":
        result = add(float(num1), float(num2))

    elif operator == "-":
        result = subtract(float(num1), float(num2))

    elif operator == "*":
        result = multiply(float(num1), float(num2))

    elif operator == "/":
        result = divide(float(num1), float(num2))
    
    elif operator == "square":
        result = square(float(num1), float(num2))

    elif operator == "cube":
        result = cube(float(num1), float(num2))

    elif operator == "pow":
        result = power(float(num1), float(num2))

    elif operator == "mod":
        result = mod(float(num1), float(num2))

    print(result)