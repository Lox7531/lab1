import numpy as np
import math
a=0.1
b=1
h=0.1
i=0
s=0
y=0
for x in np.arange(0.1,1.1,0.1):
    i+=1
    x=round(x,15)
    print("при x =", x ,"y = cosx = ", math.cos(x))
    if abs(((-1)**i)*(x**(2*i)/(math.factorial(2*i))))>=0.0001:
        s=s+((-1)**i)*(x**(2*i)/(math.factorial(2*i)))
        print(((-1)**i)*(x**(2*i)/(math.factorial(2*i))))
print("сумма =",s)

