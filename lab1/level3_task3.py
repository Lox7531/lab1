'''
Вычислить сумму s, прекращая суммирование, когда очередной член суммы по абсолютной величине станет меньше 0,0001, при изменении аргумента x в указанном диапазоне [a,b] с шагом h.
Для сравнения в каждой точке вычислить функцию, являющаюся аналитическим выражением ряда S = 1+《 cos(ix)/ i!,  y =e^cosx×cos(sinx), a = 0,1 b = 1 h = 0,1
'''
a=0.1
b=1
h=0.1
x=0
import math
for i in range(10):
    x+=h
    x=round(x,1)
    s=1
    i=1
    t=100
    while True:
        if abs(t)>0.0001:
            t=((math.cos(i*x))/math.factorial(i))
            i+=1
            s+=t
        else:
            break
    print("при x=",x,"Значение суммы:",s, "Значение y=(e^(cosx))*cos(sinx):", math.exp(math.cos(x))*math.cos(math.sin(x)))
