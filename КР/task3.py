"""
13.Из массива удалить повторяющиеся элементы.
"""
import array
print("Введите количество элементов массива")
n=int(input())
ara=[]
lst=[]
for i in range(n):
    print("Введите элемент")
    t=(input())
    ara.append(t)
print("Массив до изменения:",ara)
t=len(ara)
lst.append(ara[0])
for i in range(t):
    for j in range(i+1,t):
        if ara[i]!=ara[j]:
            lst.append(ara[j])
            break
            print(lst)
ara=lst
print(ara)
