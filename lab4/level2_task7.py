#В матрице А размером 6x6 найти максимальный элемент на главной диагонали.
#Заменить нулями элементы матрицы, расположенные правее главной диагонали в строках, расположенных выше строки, содержащей максимальный элемент на главной диагонали.
import numpy as np
maxi=-1
q=0
m=0
A=np.array([[1,100,3,4,5,6,],
   [8,9,101,11,12,13, ],
   [14,15,16,102,18,19, ],
   [20,21,22,1000,103,25, ],
   [26,27,28,29,30,104, ],
   [8,9,10,11,12,13]
   ])
print("Матрица до:")
print(A)
for i in range(len(A)):
    for j in range(len(A[0])):
        if maxi<A[i][j]:
            maxi=A[i][j]
            str=i
            stl=j
for i in range(len(A)):
    if i<str:
        while True:
            if q<=4:
                A[i][q+1]=0
                q+=1
            else:
                m+=1
                break
    q=m
print("Максимальный элемент на главной диагонали:",maxi)
print("Матрица после:")
print(A)
