f = open('26-145.txt')
n = int(f.readline())  # считываем первую строку из файла
m, k = map(int, f.readline().split())  # считываем вторую строку из файла
# создаем модель нашего поезда в виде словаря
vagons = {x: [[[0, 0, 0, 0], [0, 0]] for _ in range(k)] for x in range(1, m + 1)}
passengers = sorted(list(map(int, f.readline().split())) for i in range(n))[::-1]  # считываем наши группы
kids_set = 0
for i in passengers:  # проходимся циклом по нашим группам
    people, kids = i  # и заселяем ее на первое подходящее место в наш словарь
    status_groupe = 0  # статус нашей группы 0 - незаселена, 1 - заселена
    if people <= 2:  # когда количество людей в группе не больше двух, заселяем ее на боковые места:
        for j1 in range(1, m + 1):
            for j2 in range(len(vagons[j1])):
                for j4 in range(len(vagons[j1][j2])):
                    if len(vagons[j1][j2][j4]) == 2 and sum(vagons[j1][j2][j4]) == 0:
                        for j3 in range(people):
                            vagons[j1][j2][j4][j3] += 1
                        status_groupe = 1
                        kids_set += kids
                        break
                if status_groupe == 1:
                    break
            if status_groupe == 1:
                break
    if people > 2:  # Аналогично делаем для групп в которых больше двух людей
        for j1 in range(1, m + 1):
            for j2 in range(len(vagons[j1])):
                for j4 in range(len(vagons[j1][j2])):
                    if len(vagons[j1][j2][j4]) == 4 and sum(vagons[j1][j2][j4]) == 0:
                        for j3 in range(people):
                            vagons[j1][j2][j4][j3] += 1
                        status_groupe = 1
                        kids_set += kids
                        break
                if status_groupe == 1:
                    break
            if status_groupe == 1:
                break

max_current, v = -1, 0  # начинаем искать вагон: max_current - текущий максимум свободных мест, v - номер вагона
for i1 in vagons:  # далее проходим по нашему словарю и для каждого вагона обновляем значения max_current и v.
    c = 0
    for i2 in range(len(vagons[i1])):
        for i3 in range(len(vagons[i1][i2])):
            for i4 in range(len(vagons[i1][i2][i3])):
                if vagons[i1][i2][i3][i4] == 0:
                    c += 1
    if c > max_current:
        max_current, v = c, i1
print(kids_set, v)  # выводим ответ

f.close()