# вычислить значение функции y при заданном значении аргумента x по формуле y=1, если x<=-1, или y=-x, если -1<x<=1, или y=-1, если x>1.
import random
random.seed(5)
print(random.randint(1, 10))

x=int(input())
if x<=-1:
    y=1
    print("y =", y)
elif x>-1 and x<=1:
    y=-1*x
    print("y =", y)
elif x>1:
    y=-1
    print("y =", y)