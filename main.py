#functions for the 4 basic operations
def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def mult(num1, num2):
    return num1 * num2

def div(num1, num2):
    if num2 == 0:
        return "Error: Cnnot divide by 0"
    return num1 / num2

#main program
def calculator():
    #get user input
    num1 = float(input("Enter num 1: "))
    sign = input("Enter a sign (+, -, *, /) : ")
    num2 = float(input("Enter num 2: "))
 
 #perform the operations
    if sign == "+" :
        print("Sum: " ,add(num1, num2))
    elif sign == "-" :
        print("Subtraction: ", sub(num1,num2))
    elif sign ==  "*" :
        print("Multiplication: " ,mult(num1,num2))
    elif sign == "/" :
        print("Division: " ,div(num1,num2))
    else :
        print("Invalid operator sign.")     

#run the function
calculator()