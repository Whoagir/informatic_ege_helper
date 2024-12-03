# Автор: К. Далос

from itertools import product

c = 'СПОРТЛОТО'  # предварительно надо удалить уже имеющиеся буквы
dcc = {i: c.count(i) for i in c}
print(dcc.keys())
dcc = list(dcc.values()) + [0]  # добавляем условие, что необходимо оставить одну ветку не кодированной
cur = []
forbidden = []  # здесь будут те кодовые слова которые даны по условию и их нельзя использовать
cursum = 0
out = 1e10
best = []


def dfs():
    global out, cursum, cur, best, forbidden
    if cursum > out:  # отсеиваем заранее проигрышные результаты, чтобы ускорить работу программы
        return

    if len(cur) == 7:  # 7 = 6 букв 'С', 'П', 'О', 'Р', 'Т', 'Л' + ветка которую нужно оставить под остальной алфавит
        if out > cursum:
            best = cur.copy()
            out = min(out, cursum)
        return

    for i in range(1, 5):  # генерация всех возможных длин кодового слова
        for j in product('01', repeat=i):
            j = ''.join(j)
            f = 1
            for z in cur + forbidden:  # проверка перебираемого кодового слова на условие Фано
                ln = min(len(j), len(z))
                if z[:ln] == j[:ln]:
                    f = 0
                    break
            if f:
                cur.append(j)
                cursum += len(j) * dcc[len(cur) - 1]
                dfs()
                cursum -= len(j) * dcc[len(cur) - 1]
                cur.pop()


dfs()
print(out)
print(best)
