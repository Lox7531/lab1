'''
Найти среднее ариметическое значение эелементов массива, расположенных между
минимальным  и максимальным элементами массива
'''
f = open('level2_task9.txt', 'r+')
lst1=f.readlines()
lst=[int(i) for i in lst1]
k=0
s=0
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
    str1='\n'+"Answer:" + str(s/k)
    f.write(str1)
if mi-ma>0 and abs(mi-ma)!=1:
    for i in range(ma+1,mi):
        k+=1
        s+=lst[i]
    str1='\n'+"Answer:" + str(s/k)
    f.write(str1)
if abs(mi-ma)==1:
    print("среднее арифметическое между макс. и мин. : 0")
    str1="Answer: 0"
    f.write(str1)
print(f.read())
f.close()

