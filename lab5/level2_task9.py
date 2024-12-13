"""
9. Даны матрицы А размером 6 × 5 и С размером 7 4. Объединить
массивы, сформированные из сумм положительных элементов столб-
цов матриц А и С. Суммирование положительных элементов столбцов
получением результата в виде массива осуществить в методе.
"""
import numpy as np
summa=0
def sum_positive_elements(matrix):
    summa=0
    # Преобразуем входной список в массив NumPy для удобства операций
    np_matrix = np.array(matrix)
    # Суммируем положительные элементы по столбцам
    positive_sums=[]
    for i in range(len(np_matrix[0])):
        for j in range(len(np_matrix)):
            if np_matrix[j][i]>0:
                summa+=np_matrix[j][i]
        positive_sums.append(summa)
        summa=0
    return positive_sums

def main():
    # Пример матрицы A размером 6x5
    A = [
        [1, -2, 3, 4, 5],
        [6, 7, -8, 9, -10],
        [-11, 12, 13, -14, 15],
        [16, -17, 18, 19, -20],
        [21, 22, -23, 24, 25],
        [-26, 27, 28, 29, 30]
    ]

    # Пример матрицы C размером 7x4
    C = [
        [1, -2, 3, 4],
        [-5, 6, -7, 8],
        [9, 10, -11, 12],
        [-13, 14, 15, -16],
        [-17, 18, -19, 20],
        [21, 22, -23, -24],
        [25, -26, 27, 28]
    ]

    # Суммируем положительные элементы столбцов
    sum_A = sum_positive_elements(A)
    sum_C = sum_positive_elements(C)

    # Объединяем массивы
    combined_result = np.concatenate((sum_A, sum_C))

    print("Суммы положительных элементов в столбцах матрицы A:", sum_A)
    print("Суммы положительных элементов в столбцах матрицы C:", sum_C)
    print("Объединенные результаты:", combined_result)

if __name__ == "__main__":
    main()
import numpy as np

def sum_positive_elements(matrix):
    # Преобразуем входной список в массив NumPy для удобства операций
    np_matrix = np.array(matrix)
    # Суммируем положительные элементы по столбцам
    positive_sums = np.sum(np_matrix * (np_matrix > 0), axis=0)
    return positive_sums

def main():
    # Пример матрицы A размером 6x5
    A = [
        [1, -2, 3, 4, 5],
        [6, 7, -8, 9, -10],
        [-11, 12, 13, -14, 15],
        [16, -17, 18, 19, -20],
        [21, 22, -23, 24, 25],
        [-26, 27, 28, 29, 30]
    ]

    # Пример матрицы C размером 7x4
    C = [
        [1, -2, 3, 4],
        [-5, 6, -7, 8],
        [9, 10, -11, 12],
        [-13, 14, 15, -16],
        [-17, 18, -19, 20],
        [21, 22, -23, -24],
        [25, -26, 27, 28]
    ]

    # Суммируем положительные элементы столбцов
    sum_A = sum_positive_elements(A)
    sum_C = sum_positive_elements(C)

    # Объединяем массивы
    combined_result = np.concatenate((sum_A, sum_C))

    print("Суммы положительных элементов в столбцах матрицы A:", sum_A)
    print("Суммы положительных элементов в столбцах матрицы C:", sum_C)
    print("Объединенные результаты:", combined_result)

if __name__ == "__main__":
    main()
