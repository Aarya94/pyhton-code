"""
name = input("Enter your first name: ")
food = input("Enter your favorite food: ")
age = int(input("Enter your age: "))
print(f"Hello {name}, your favorite food is {food}.")
print(f"Thank you for sharing {name}!")
print(type(name), type(food), type(age))
k=name + food + str(age)
print(k)
"""
"""
while True:
    length = float(input("Enter the length of a  number: "))
    if length <= 0:
        print("Length cannot be zero or negative")
    else:
        break

while True:
    breadth = float(input("Enter the breadth of a  number: "))
    if breadth <= 0:
        print("Breadth cannot be zero or negative")
    else:
        break

area = length * breadth
print(f"The area of the rectangle is: {area}")
"""

"""
def input_checker(prompt, type_=float, min_=1):
    while True:
        try:
            value = type_(input(prompt))
            if value < min_:
                print(f"Value must be greater than or equal to {min_}.")
            else:
                return value
        except ValueError:
            print(f"Please enter a valid {type_.__name__}.")

length = input_checker("Enter the length of a rectangle: ")
breadth = input_checker("Enter the breadth of a rectangle: ")
area = length * breadth
print(area)
"""
"""
item_no = 0
item={1:"apple",2:"banana",3:"orange"   }
quantity={item[1]:0,item[2]:0,item[3]:0}
price = {item[1]:1.0,item[2]:2.0,item[3]:3.0}
value = input("do you want to add an item to the list? (y/n): ")
while value.lower() == 'y':
    print("Available items:")
    for key, value in item.items():
        print(f"{key}. {value}")
    print(item)
    my_list = list(item.items())

    print(my_list)
    
    item_no = int(input("Enter the item number: "))
    item_name = item.get(item_no, None)
    if item_name is None:
        print("Invalid item number.")
        continue
    else:

        print(f"You selected: {item_name}")
        qty = int(input("Enter the quantity : "))
        quantity[item_name] = qty
        p = qty * price.get(item_name, 0)
        price[item_name] = p
        value = input("do you want to add another item to the list? (y/n): ")
        print(f"your total bill is: {sum(price.values())}")
"""
"""
#calculate the circumference of a circle
import math
radius = float(input("Enter the radius of the circle: "))
circumference = 2 * math.pi * radius
print(f"The circumference of the circle is: {circumference}")
"""
"""
#calculate the area of a circle
import math
from turtle import circle
radius = float(input("Enter the radius of the circle: "))
area = math.pi * radius ** 2
area2 = math.pi * pow(radius, 2)
print(f"The area of the circle is: {area}")
print(f"The area of the circle is: {area2}")
"""
"""
#hypothenuse of a right triangle
import math
height = float(input("Enter the height of the triangle: "))
bredth = float(input("Enter the breadth of the triangle: "))
hypotenuse = math.sqrt(height ** 2 + bredth ** 2)
print(f"The hypotenuse of the triangle is: {hypotenuse}")
"""

"""
#boolean if
online = True
if online:
    print("You are online")
else:
    print("You are offline")
"""

"""
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
"""
"""
#weight converter

def weight_conv():
    value=input("conversion from kg to gram ? y/n  ")
    if value.lower ()=="y":
        w_kg= float(input("enter the weight in killograms"))
        print(w_kg * 1000 ," converted to grams")
    else:
        w_g=float(input("enter the weight in grams"))
        print(w_g/1000 ,"converted to killograms")

print("welcome to weight converter")
weight_conv()
"""

"""
#name checker
name = input("enter your name: ")
def name_check():
        global name

        if 1<=len(name)<=12:
            if " " not in name:
                if name.isalpha():
                    print("input saved")
                else:
                    name= input("enter name having alphabets only : ")
                    name_check()
            else:
                name=input("print name without space : ")
                name_check()
        else:
            name=input ("name should be of 12 character only : ")
            name_check()
name_check()
"""
"""
#interest calculator 

#simple interest
p=float( input("enter the amount for interest calculation") )
r=float(input("enter the rate for interest calculation"))
def simple_int():
    f=input("time period for interest calculation is in months or year : m/y ?")
    while f.lower() not in ("y","m"):
        f=input("Enter y for years or m for months:")
    t=float(input("enter the time in year for interest calculation "))
    if f.lower()=="y":
        print ("your total interest is ",(p*r*t)/100)
        print("your total amount is : ", p+(p*r*t)/100)
    else:
        t=t/12
        print ("your total interest is ",(p*r*t)/100)
        print("your total amount is : ", p+(p*r*t)/100)

#compound interest
def com_int():
    f=input("how is your interest calculated ,enter \n1. 'a' for annually \n2. 'h' for half yearly \n3. 'q' for quaterly \n4. 'd' for daily \n \n if your interest is compunded at specific month , enter 'm' .\n your choice :  " )
    while f.lower() not in ("m","a","h","q","d"):
        f=input("enter \n1. 'a' for annually \n2. 'h' for half yearly \n3. 'q' for quaterly \n4. 'd' for daily \n \n if your interest is compunded at specific month , enter 'm'")
    check=input ("you are entering the time in months or year ? \n m for months \n y for year : ")
    while check.lower() not in ("m","y"):
        check =input("enter m for months or y for years")
    if check=="m":
        t=float(input("enter the time for compounding your interest in months"))
        t=float(t/12)
        match f :
            case "a":
                amount= p*(1+r/ (100*1))**(1*t)
                print (f"your compound interest is {amount - p:.2f} ")
                print(f"your compounded total amount is {amount:.2f}")
            case "h":
                amount= p*(1+r/ (100*2))**(2*t)
                print (f"your compound interest is {amount - p:.2f} ")
                print(f"your compounded total amount is {amount:.2f}")
            case "q":
                amount= p*(1+r/ (100*4))**(4*t)
                print (f"your compound interest is {amount - p:.2f} ")
                print(f"your compounded total amount is {amount:.2f}")
            case "d":
                l=input("is this a leap year ?  y/n")
                while l.lower() not in ("y", "n"):
                    l=input("is this a leap year ? y/n")
                if l.lower()=="y":
                    amount= p*(1+r/ (100*366))**(366*t)
                    print (f"your compound interest is {amount - p:.2f} ")
                    print(f"your compounded total amount is {amount:.2f}")
                else:
                    amount= p*(1+r/ (100*365))**(365*t)
                    print (f"your compound interest is {amount - p:.2f} ")
                    print(f"your compounded total amount is {amount:.2f}")
            case "m":
                k=float(input("enter the no of month for your interst calculation"))
                n=k/12
                amount= p*(1+r/ (100*n))**(n*t)
                print (f"your compound interest is {amount - p:.2f} ")
                print(f"your compounded total amount is {amount:.2f}")
    else:
        t=float(input("enter the time for compounding your interest in years"))
        match f :
            case "a":
                amount= p*(1+r/ (100*1))**(1*t)
                print (f"your compound interest is {amount - p:.2f} ")
                print(f"your compounded total amount is {amount:.2f}")
            case "h":
                amount= p*(1+r/ (100*2))**(2*t)
                print (f"your compound interest is {amount - p:.2f} ")
                print(f"your compounded total amount is {amount:.2f}")
            case "q":
                amount= p*(1+r/ (100*4))**(4*t)
                print (f"your compound interest is {amount - p:.2f} ")
                print(f"your compounded total amount is {amount:.2f}")
            case "d":
                l=input("is this a leap year ?  y/n")
                while l.lower() not in ("y", "n"):
                    l=input("is this a leap year ? y/n")
                if l.lower()=="y":
                    amount= p*(1+r/ (100*366))**(366*t)
                    print (f"your compound interest is {amount - p:.2f} ")
                    print(f"your compounded total amount is {amount:.2f}")
                else:
                    amount= p*(1+r/ (100*365))**(365*t)
                    print (f"your compound interest is {amount - p:.2f} ")
                    print(f"your compounded total amount is {amount:.2f}")
            case "m":
                k=float(input("enter the time in month at which you will be interested at "))
                n=12/k
                amount= p*(1+r/ (100*n))**(n*t)
                print (f"your compound interest is {amount - p:.2f} ")
                print(f"your compounded total amount is {amount:.2f}")
z=input("which interest you wanna calculate , simple or compound ? s/c : ")
while z.lower() not in ("s","c"):
    z=input("enter s for simple interest calculation and c for compound interest calculatoin")
if z.lower()=="s":
    simple_int()
else:
    com_int()
"""

"""
# timer



"""