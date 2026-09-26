import time
h=0
m=0
def timer():
    global h , m
    while True:
        for i in range(60):
            time.sleep(1)
            print (f"{h:02d}:{m:02d}:{i:02d}")
        m+=1
        if m==60:
            m=0
            h+=1
            if h==24:
                h=0
def stopwatch():
    h=int(input("enter hour : "))
    m=int(input("enter minnutes : "))
    s=int(input("enter seconds : "))
    while True:
        for i in reversed (range (s+1)):
            time.sleep(1)
            print(f"{h:02d}:{m:02d}:{i:02d}")
            if h==0 and m==0 and i==0:
                print("TIME'S UP !!")
                return
        s=59
        if i>0:
            m-=1
        elif h>0:
            h-=1
            m=59

a=input("1. timer or\n2. stopwatch : ")
while a not in("1","timer","2","stopwatch"):
    a=input("choose a valid option : ")
if a=="1"or a=="timer":
    timer()
else:
    stopwatch()