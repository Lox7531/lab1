"""
Максимальный элемент массива среди элементов с четными индексами заменить значением его индекса.
"""
import array
print("Введите количество элементов массива")
maxi=-1
n=int(input())
ara=[]
for i in range(n):
    print("Введите элемент")
    t=int(input())
    ara.append(t)
print("Массив до изменения:",ara)
for i in range(len(ara)):
    if i%2==0:
        maxi=max(ara[i],maxi)
for i in range(len(ara)):
    if ara[i]==maxi:
        ara[i]=i
print("Массив принимает вид:",ara)
