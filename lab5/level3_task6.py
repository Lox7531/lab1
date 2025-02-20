'''
Поменять местами столбец, содержащий максимальный эле-
мент на главной диагонали заданной квадратной матрицы, со столб-
цом, содержащим максимальный элемент в первой строке матрицы.
Для замены столбцов использовать метод.
'''
import numpy as np
#пример квадратной матрицы
A =np.array([[60, 2, 1000],
              [4, 100, 6],
              [7, 8, 0]]
            )
#на главной диагонали max элемент '100', в первой строчке '1000'
print("Матрица до:")
for i in range(len(A)):
    for j in range(len(A[i])):  
        print(A[i][j], end=' ')
    print()
def swap(matrix):
    max1=-100
    # Нахождение индекса максимального элемента на главной диагонали
    for i in range(len(matrix)):
        if max1<matrix[i][i]:
            max1=max(max1,matrix[i][i])
            index=i
    # Нахождение индекса максимального элемента в первой строке
    index2 = np.argmax(matrix[0])
    # Проверка, нужно ли производить обмен
    if index!=index2:
        for i in range(len(matrix)):
            c = matrix[i][index]
            matrix[i][index] = matrix[i][index2]
            matrix[i][index2] = c
        
    return matrix
print("Матрица после того, как поменяли столбцы местами:")
A=swap(A)
for i in range(len(A)):
    for j in range(len(A[i])):  
        print(A[i][j], end=' ')
    print()
