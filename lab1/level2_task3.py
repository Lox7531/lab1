'''
Определить количество членов арифметической прогрессии, сумма которых s=a+(a+h)+...+(a+hn) не превышает заданного числа p.
'''
print("Введите первый член прогрессии a:")
a=int(input())
print("Введите разность арифметической прогрессии h:")
h=int(input())
print("Введите число p:")
p=int(input())
s=a
n=0
i=1
while s<=p:
    i+=1
    n+=1
    s+=(a+n*h)
i=i-1
print("Количество членов прогрессии, сумма которых не превышает p:",i)