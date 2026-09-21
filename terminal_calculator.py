# calculator
import math
import os
num = 0
value = "0"
operator = ["+", "-", "*", "/", "**","sqrt","=","."]
def display():
    # Clear terminal
    os.system("cls" if os.name == "nt" else "clear")
    # Calculator display
    print(value)
    print()
    # Calculator buttons
    num = 0
    for i in range(5):
        for j in range(2):
            if num <= 9:
                print(num, end=" ")
                num += 1
        print(operator[i])
    print()
# START CALCULATOR
print("Welcome to the calculator!")
display()
# First number
input1 = input("")
# CALCULATION LOOP
while True:
    # Current value becomes the display
    value = str(input1)
    display()
    # Ask for operator
    if input1 in operator:
        if input1 == "sqrt":
            input2 =int(input(""))
            result = math.sqrt(float(input2))
            value = str(result)
            input1 = result
            display()
        elif input1 == "=":
            result =0
            value = str(result)
            input1 = result
            display()
        else:
            if input1 in operator[0:2]:
                input2 = input("")
                result = input2
                value = str(result)
                display()
            elif input1 in operator[2:5]:
                input2 = input("")
                result = 0
                value = str(result)
                display()
    else:
        input2 = input("")
        value = str(input1)+ str(input2)
        display()
        match input2:
            case "+":
                input3 =int(input(""))
                value = str(input1) + str(input2) + str(input3)
                display()
                result = int(input1) + int(input3)
                value = str(result)
                input1 = result
                display()
            case "-":
                input3 =int(input(""))
                value = str(input1) + str(input2) + str(input3)
                display()
                result = int(input1) - int(input3)
                value = str(result)
                input1 = result
                display()
            case "*":
                input3 =int(input(""))
                value = str(input1) + str(input2) + str(input3)
                display()
                result = int(input1) * int(input3)
                value = str(result)
                input1 = result
                display()
            case "/":
                input3 =int(input(""))
                value = str(input1) + str(input2) + str(input3)
                display()
                result = int(input1) / int(input3)
                value = str(result)
                input1 = result
                display()
            case "=":
                break
