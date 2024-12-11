'''
5. Группе студентов в результате полусеместровой аттестации
были выставлены оценки по информатике, а также определено коли-
чество пропущенных занятий. Успеваемость каждого студента оцени-
вается следующими баллами: «0» (неаттестован), «2», «3», «4» или
«5». Вывести список неуспевающих (оценка «2») студентов в порядке
убывания количества пропущенных ими занятий.

'''

class Student:
    def __init__(self, name, grade, missed_classes):
        self.name = name
        self.grade = grade
        self.missed_classes = missed_classes

    def __repr__(self):
        return f"{self.name}: {self.grade}, missed: {self.missed_classes}"

# Функция для вывода неуспевающих студентов
def print_failing_students(students):
    # Фильтруем студентов с оценкой «2»
    failing_students = [student for student in students if student.grade == 2]

    # Сортируем по количеству пропущенных занятий в порядке убывания
    failing_students.sort(key=lambda x: x.missed_classes, reverse=True)

    # Выводим результат
    print("Неуспевающие студенты (оценка 2):")
    for student in failing_students:
        print(student)

students = [
    Student("Иванов И.И.", 3, 5),
    Student("Петров П.П.", 2, 2),
    Student("Сидоров С.С.", 5, 0),
    Student("Кузнецова А.А.", 2, 8),
    Student("Смирнов А.А.", 4, 3),
    Student("Федоров В.В.", 2, 4)
]

print_failing_students(students)
