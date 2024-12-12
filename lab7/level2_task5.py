'''
5. Соревнования по прыжкам на лыжах со 120-метрового трам-
плина оценивают 5 судей. Каждый судья выставляет оценку за стиль
прыжка по 20-балльной шкале. Меньшая и большая оценки отбрасы-
ваются, остальные суммируются. К этой сумме прибавляются очки
дальность прыжка: 120 м - 60 очков, за каждый метр превышения
добавляются по 2 очка, при меньшей дальности отнимаются 2 очка
каждый метр. Получить итоговую таблицу соревнований, содержа-
щую фамилию и итоговый результат для каждого участника в поряд-
ке занятых мест.
'''
class Jumper:
    def __init__(self, name):
        self.name = name
        self.style_scores = []
        self.distance = 0
    def add_style_score(self, score):
        if 0 <= score <= 20:
            self.style_scores.append(score)
    def set_distance(self, distance):
        self.distance = distance
    def calculate_result(self):
        if len(self.style_scores) < 3:
            return None
        # Отбрасываем наименьшую и наибольшую оценки
        sorted_scores = sorted(self.style_scores)[1:-1]
        style_score_sum = sum(sorted_scores)
        # Рассчитываем очки за дальность
        distance_score = 60 + (self.distance - 120) * 2 if self.distance > 120 else 60 + (self.distance - 120) * 2
        return style_score_sum + distance_score
def main():
    jumpers = [Jumper('Иванов'), Jumper('Петров'), Jumper('Сидоров')]
    # Пример добавления оценок и расстояний
    jumpers[0].add_style_score(18)
    jumpers[0].add_style_score(19)
    jumpers[0].add_style_score(17)
    jumpers[0].set_distance(130)
    jumpers[1].add_style_score(20)
    jumpers[1].add_style_score(18)
    jumpers[1].add_style_score(19)
    jumpers[1].set_distance(125)
    jumpers[2].add_style_score(15)
    jumpers[2].add_style_score(14)
    jumpers[2].add_style_score(13)
    jumpers[2].set_distance(110)
    results = [(jumper.name, jumper.calculate_result()) for jumper in jumpers]
    results = sorted(results, key=lambda x: x[1], reverse=True)
    for place, (name, score) in enumerate(results, start=1):
        print(f"{place}. {name}: {score}")
if __name__ == "__main__":

    main()

