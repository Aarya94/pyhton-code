import time
h=0
m=0
s=0
#stopwatch
def stopwatch():
    global h,m,s
    while True:
        for i in range(60):
            s=i
            time.sleep(1)
            print(f"{h:02d}:{m:02d}:{s:02d}")
        m+=1
        s=0
        if m==60:
            m=0
            h+=1
"""
h, m, s = map(int, input("Enter time (hours minutes seconds): ").split())
print (h)
print(s)
print(m)
"""

#timer
def timer()
    h = int(input("enter hours : "))
    m = int(input("enter minutes : "))
    s = int(input("enter seconds : "))
    t = h*3600+m*60+s
    m =int(t%3600)//60
    h =int(t//3600)
    s =int(t%60)
    for i in reversed(range(t+1)):
        time.sleep(1)
        print(f"{h:02d}:{m:02d}:{s:02d}")
        if s>0:
            s-=1
        if m>0
            m-=1
            s=59
        if h!=0 and m==0:
                h-=1
                m=59
    print("time's up!!!")


a=input("1. timer or\n2. stopwatch : ")
while a not in("1","timer","2","stopwatch"):
    a=input("choose a valid option : ")
if a=="1"or a=="timer":
    timer()
else:
    stopwatch()






