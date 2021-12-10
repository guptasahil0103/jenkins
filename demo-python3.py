def addition(x ,y):
    return x + y
def subtraction(x ,y):
    return x - y
def multiplication(x ,y):
    return x * y
def division(x ,y):
    return x / y 

print("1. addition")
print("2. subtraction")
print("3. multiplication")
print("4. division")

operation = int(input("Please Enter the operation: "))

number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

if operation == 1:
    print(number1, " + ", number2, " = ",
        addition(number1,number2))
elif operation == 2:
    print(number1, " - ", number2, " = ",
        subtraction(number1,number2))
elif operation == 3:
    print(number1, " * ", number2, " = ",
        multiplication(number1,number2))
elif operation == 4:
    try:
        print (number1, '/', number2, '=', division(number1/number2))
    except ZeroDivisionError:
        print (number1, '/', number2, ':', 'Division by zero!')
else :
    print("Invalid Selection operation is selected") 
exit()           

