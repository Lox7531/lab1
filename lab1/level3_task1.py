a=0.1
b=1
h=0.1
x=0
s=0
i=0
t=100
import math
for i in range(10):
    x+=h
    x=round(x,1)
    s=0
    i=0
    t=100
    while True:
        if abs(t)>0.0001:
            t=((-1)**i)*((x**(2*i))/math.factorial(2*i))
            i+=1
            s+=t
        else:
            break
    print("при x=",x,"Значение суммы:",s, "Значение y=cosx:", math.cos(x))
