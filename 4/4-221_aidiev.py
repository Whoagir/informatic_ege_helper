from itertools import *

# входные данные
alp = 'ПРOСТЕГЭ'  # исходный алфавит
word = 'ПРOСТOЕГЭ'  # слово, которые нужно найти
known = {'П': '1111', 'Р': '110', 'С': '11101', 'Т': '00', 'Е': '11100'}  # буквы, код которых уже знаем
dic = [0] * 20
dic[2] = 2  # список свободных веток

freq = {i: word.count(i) for i in set(alp)}  # сколько раз встречается каждая буква алфавита в слове
len_known = sum([len(j) * freq[i] for i, j in known.items()])  # длина кода, который мы уже знаем
unknown = sorted([j for i, j in freq.items() if i not in known], reverse=1)  # сколько раз встречается каждая буква алфавита, которую мы не знаем в слове


def iter(dic, comb):  # код прохода по одной итерации
    for i in comb:
        if dic[i] == 0:
            return [0]
        dic[i] -= 1
        dic[i + 1] += 2
    return dic  # возвращает кол-во свободных веток


def lenn(dic, mas):  # подсчитывает длину каждой итерации
    if sum(dic) < len(mas):  # если свободных мест меньше, чем нужных
        return 100000000
    su = 0
    for i in mas:
        for j in range(len(dic)):
            if dic[j] != 0:
                su += i * j
                dic[j] -= 1
                break
    return su  # возвращает суммарную длину кода


minn = lenn(list(dic), unknown)  # первоначальная позиция
for i in range(1, 7):
    for j in product(range(1, 7), repeat=i):  # перебираем различные действия (итерации)
        minn = min(lenn(iter(list(dic), j), unknown), minn)  # ищем минимум
print(minn + len_known)  # нашли его
