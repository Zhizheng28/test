def addition(num1, num2):
    result = num1 + num2
    print("{0} + {1} = {2}".format(num1, num2, result))

def subtraction(num1, num2):
    result = num1 - num2
    print("{0} - {1} = {2}".format(num1, num2, result))

def multipication(num1, num2):
    result = num1 * num2
    print("{0} * {1} = {2}".format(num1, num2, result))

def division(num1, num2):
    if num2 == 0.0:
        print("Can't Divide by Zero ")
    else:
        result = num1 / num2
        print("{0} / {1} = {2}".format(num1, num2, result))

