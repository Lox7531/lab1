#вычислить сумму s=cosx+(cos(2x))/2^2+...+(cosnx)/n^2+...
#cуммирование прекратить, когда очередной член суммы по модулю будет меньше e=0.0001
s=0
import math
print("Введите x")
x=int(input())
t=100
n=1
while True:
    if abs(t)>0.0001:
        t=(math.cos(n*x))/(n**2)
        s+=t
        n+=1
    else:
        break
print("Сумма равна",s)
