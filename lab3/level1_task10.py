'''
Дан одномерный массив размера 10 и два числа P и Q (P < Q).
Определить сколько элементов массива заключено между P и Q .
'''
p=2
q=7
lst=[1,2,3,4,5,6,7,8,9,10]
for i in range(len(lst)):
    if lst[i]==p:
        t=i #1
    if lst[i]==q:
        r=i #6
print("Количество элементов между p и q:",(r-t-1))
