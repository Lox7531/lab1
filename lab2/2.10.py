#в группе учится n студентов. Каждый получил на экзаменах по 4 оценки. Подсчитать число студентов, не имеющих "2" и "3".
import random
random.seed(5)
print(random.randint(1, 13))
n=int(input())
k=0
for i in range(n):
    print("Введите 1-ую оценку:")
    x1 = int(input())
    print("Введите 2-ую оценку:")
    x2= int(input())
    print("Введите 3-ую оценку:")
    x3= int(input())
    print("Введите 4-ую оценку:")
    x4= int(input())
    if x1>3 and x2>3 and x3>3 and x4>3:
        k+=1
print(k)
