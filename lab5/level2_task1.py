'''
1.Поменять местами максимальные элементы матриц
А размером 5 × 6 и В размером 3 × 5.
Поиск максимального элемента матрицы осуществить в методе.
'''
import numpy as np
A = np.array([
        [1, -2, 3, 4, 5,7],
        [6, 7, -8, 9, -10,9],
        [-11, 12, 13, -14, 15,10],
        [16, -17, 18, 19, -20,11],
        [21, 22, -23, 24, 25,12],
        ])
print('Матрица A до:')
for i in range(len(A)):
        for j in range(len(A[i])):  
            print(A[i][j], end=' ')
        print()
B =np.array ([
        [1, -2, 3, 4, 5],
        [6, 7, -8, 9, -10],
        [-11, 12, 13, -14, 15],
        ])
print('Матрица B до:')
for i in range(len(B)):
        for j in range(len(B[i])):  
            print(B[i][j], end=' ')
        print()
def swapi(m1,m2):
    maxi1=m1[0][0]
    i1=0
    j1=0
    for i in range(len(m1)):
        for j in range(len(m1[0])):
            if m1[i][j]>maxi1:
                maxi1=m1[i][j]
                i1=i
                j1=j
    maxi2=m2[0][0]
    i2=0
    j2=0
    for i in range(len(m2)):
        for j in range(len(m2[0])):
            if m2[i][j]>maxi2:
                maxi2=m2[i][j]
                i2=i
                j2=j
    m1[i1][j1], m2[i2][j2] = m2[i2][j2], m1[i1][j1]
    print('Матрица А после:')
    for i in range(len(m1)):
        for j in range(len(m1[i])):  
            print(m1[i][j], end=' ')
        print()
    print('Матрица B после:')
    for i in range(len(m2)):
        for j in range(len(m2[i])):  
            print(m2[i][j], end=' ')
        print()
swapi(A,B)
