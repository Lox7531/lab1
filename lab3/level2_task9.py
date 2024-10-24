'''
Найти среднее ариметическое значение эелементов массива, расположенных между
минимальным  и максимальным элементами массива
'''
lst=[]
k=0
s=0
print("Введите количество элементов массива")
n=int(input())
for i in range(n):
    print("Введите элемент(без повторов)")
    t=(int(input()))
    lst.append(t)
maxi=max(lst)
mini=min(lst)
for i in range(len(lst)):
    if lst[i]==maxi:
        ma=i
    if lst[i]==mini:
        mi=i
if ma>mi and abs(mi-ma)!=1:
    for i in range(mi+1,ma):
        k+=1
        s+=lst[i]
        print(lst[i])
    print("среднее арифметическое между макс. и мин. :",(s/k))
    
if mi-ma>0 and abs(mi-ma)!=1:
    for i in range(ma+1,mi):
        k+=1
        s+=lst[i]
    print("среднее арифметическое между макс. и мин. :",(s/k))
if abs(mi-ma)==1:
    print("среднее арифметическое между макс. и мин. : 0")

