#вычислить s=1!+2!+...+6!
import math
s=0
for i in range(1,7):
    s+=math.factorial(i)
print("Сумма s=1!+2!+...+6! равна",s)
