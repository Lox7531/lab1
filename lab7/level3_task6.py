from collections import Counter

class SurveyResponse:
    def __init__(self):
        self.animals = []
        self.characteristics = []
        self.objects = []

    def add_response(self, animal, characteristic, obj):
        if animal:
            self.animals.append(animal)
        if characteristic:
            self.characteristics.append(characteristic)
        if obj:
            self.objects.append(obj)

    def get_most_common(self, data, top_n=5):
        counter = Counter(data)
        most_common = counter.most_common(top_n)
        total_responses = sum(counter.values())
        results = [(item, count, (count / total_responses * 100) if total_responses > 0 else 0) for item, count in most_common]
        return results

    def display_results(self):
        print("Наиболее часто встречающиеся ответы:")

        print(" Животные ассоциируемые с Японией:")
        animal_results = self.get_most_common(self.animals)
        self._display_results(animal_results)

        print(" Черты характера японцев:")
        characteristic_results = self.get_most_common(self.characteristics)
        self._display_results(characteristic_results)

        print(" Неодушевленные предметы или понятия, ассоциируемые с Японией:")
        object_results = self.get_most_common(self.objects)
        self._display_results(object_results)

    def _display_results(self, results):
        if not results:
            print("Нет ответов.")
            return
        print(f"{'Ответ':<30} {'Количество':<10} {'Доля (%)':<10}")
        for item, count, percentage in results:
            print(f"{item:<30} {count:<10} {percentage:.2f}")

# Пример использования
if __name__ == "__main__":
    survey = SurveyResponse()

    # Пример данных, которые могли бы быть собраны из опроса
    responses = [
        ("кот", "вежливость", "сакура"),
        ("кот", "сдержанность", "самурай"),
        ("панда", "дружелюбие", "храм"),
        ("дракон", "скромность", "вулкан"),
        ("кошка", "вежливость", "суши"),
        ("кошка", "доброта", None),
        (None, None, "культура"),
        (None, "честность", None),
        ("кот", None, "суши"),
        ("тануки", "чистоплотность", "суши"),
        ("олень", "чистоплотность", "технологии"),
        ("тунец", "бережливость", "суши"),
        ("тануки", "внимательность", "вулкан"),
    ]

    for animal, characteristic, obj in responses:
        survey.add_response(animal, characteristic, obj)

    survey.display_results()
