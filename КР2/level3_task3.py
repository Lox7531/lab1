"""
3. В соревнованиях участвуют три команды по 6 человек. Резуль-
таты соревнований представлены в виде мест участников каждой ко-
манды (1 - 18). Определить команду-победителя, вычислив количе-
ство баллов, набранное каждой командой. Участнику, занявшему 1-е
место, начисляется 5 баллов, 2-е - 4, 3-е - 3, 4-е - 2, 5-е - 1, осталь-
ным - 0 баллов. При равенстве баллов победителем считается коман-
да, за которую выступает участник, занявший 1-е место.
"""
class Team:
    def __init__(self, name, results):
        self.name = name  # Имя команды
        self.results = results  # Места участников
        self.score = 0  # Итоговый балл команды
    def calculate_score(self):
        # Считаем баллы за места
        for position in self.results:
            if position == 1:
                self.score += 5
            elif position == 2:
                self.score += 4
            elif position == 3:
                self.score += 3
            elif position == 4:
                self.score += 2
            elif position == 5:
                self.score += 1
def determine_winner(teams):
    for team in teams:
        team.calculate_score()  # Вычисляем баллы для каждой команды
    # Сортируем команды по баллам и по местоположению 1-го участника
    teams.sort(key=lambda x: (-x.score, x.results[0]))
    return teams[0]  # Возвращаем команду-победителя
# Пример использования
team1 = Team("Команда A", [1, 5, 3, 4, 6, 2])
team2 = Team("Команда B", [2, 3, 1, 5, 4, 6])
team3 = Team("Команда C", [3, 4, 6, 2, 5, 1])
winner = determine_winner([team1, team2, team3])
print(f"Победитель: {winner.name} с {winner.score} баллами")

