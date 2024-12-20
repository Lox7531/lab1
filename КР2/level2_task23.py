"""
В двух заданных матрицах по пять наибольших элементов увеличить вдвое, остальные вдвое уменьшить. 
Преобразование матрицы оформить в виде метода.
"""
import numpy as np
A = np.array([
        [10, 20, 30],
        [14, 12, 13], 
        [18, 44, 60],
        [68, 98, 90]
        ])
print("Изначальная матрица A:")
for i in range(len(A)):
        for j in range(len(A[i])):  
            print(A[i][j], end=' ')
        print()
B =np.array ([
        [14, 22, 34, 44, 54],
        [66, 76, 78, 72, 74],
        [12, 44, 22, 14, 10],
        ])
print("Изначальная матрица B:")
for i in range(len(B)):
        for j in range(len(B[i])):  
            print(B[i][j], end=' ')
        print()
def fun(M):
    lst=[]
    for i in range(len(M)):
        for j in range(len(M[0])):
            lst.append(M[i][j])
    lst.sort()
    lst=lst[::-1]
    lst=lst[:5]
    for i in range(len(M)):
        for j in range(len(M[0])):
            if lst[0]==M[i][j] or lst[1]==M[i][j] or lst[2]==M[i][j] or lst[3]==M[i][j] or lst[4]==M[i][j]:
                M[i][j]=2*M[i][j]
            else:
                M[i][j]=M[i][j]/2
    print("Матрица после:")
    for i in range(len(M)):
            for j in range(len(M[i])):  
                print(M[i][j], end=' ')
            print()
print("Для А:")
fun(A)
print("Для B:")
fun(B)
