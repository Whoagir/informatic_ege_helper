# Автор: А. Куканова

from itertools import product

WORD = 'ОНИКС'
count = 0
for k in range(4, 7):
    words = [w for w in product(WORD, repeat=k) if w.count('С') == 3 and w.count('О') == 1]
    count += len(words)
print(count)


# Михлин Б.С.
'''
8.221 (А. Куканова) Лиза составляет слова из букв О, Н, И, К, С, причём буква С должна встречаться в этих словах ровно 3 раза,
а буква О — ровно 1 раз. Длина слова составляет от 4 до 6 букв.
Сколько различных слов может составить Лиза?
'''
n=0
for a in 'оникс':
    for b in 'оникс':
        for c in 'оникс':
            for d in 'оникс':
                w=a+b+c+d
                if w.count('с')==3 and w.count('о')==1:
                    n+=1
for a in 'оникс':
    for b in 'оникс':
        for c in 'оникс':
            for d in 'оникс':
                for e in 'оникс':
                    w=a+b+c+d+e
                    if w.count('с')==3 and w.count('о')==1:
                        n+=1
for a in 'оникс':
    for b in 'оникс':
        for c in 'оникс':
            for d in 'оникс':
                for e in 'оникс':
                    for f in 'оникс':
                        w=a+b+c+d+e+f
                        if w.count('с')==3 and w.count('о')==1:
                            n+=1
print(n) # Ответ: 604