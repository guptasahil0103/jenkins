


def add(x, y): # addition
    return x + y

def subtract(x, y): #subtraction
    return x - y

def multiply(x, y): #multiply
    return x * y

def divide(x, y):  #division
    return x / y
 
print("1.Addition")
print("2.Subtraction")
print("3. Multiply")
print("4.division")

select = int(input("Select operations form 1, 2, 3, 4 :"))

number_1 = int(input("Enter first number: "))
number_2 = int(input("Enter second number: "))
  
if select == 1:
    print(number_1, "+", number_2, "=",
                    add(number_1, number_2))
  
elif select == 2:
    print(number_1, "-", number_2, "=",
                    subtract(number_1, number_2))
  
elif select == 3:
    print(number_1, "*", number_2, "=",
                    multiply(number_1, number_2))
  
elif select == 4:
    print(number_1, "/", number_2, "=",
                    divide(number_1, number_2))
else:
    print("Invalid input")