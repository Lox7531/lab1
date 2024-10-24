'''
из массива размером 12 удалить все отрицательные эелементы
'''
n=12
lst=[]
for i in range(n):
    print("Введите элемент")
    t=(int(input()))
    lst.append(t)
ara=[]
for i in range(len(lst)):
    if lst[i]>=0:
        ara.append(lst[i])
lst=ara
print("Список без отрицательных элементов:",lst)
