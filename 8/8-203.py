# Автор: А. Куканова

from itertools import permutations

consonants = 'ЛГРФМ'
vowels = 'ОАИ'
even = (0, 2, 4)
odd = (1, 3)

count = 0
for w in permutations('ЛОГАРИФМ', r=5):
    if (all(w[i] in vowels for i in even) and all(w[i] in consonants for i in odd)
            or all(w[i] in consonants for i in even) and all(w[i] in vowels for i in odd)):
        count += 1
print(count)