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
    