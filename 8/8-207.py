# Автор: А. Куканова

from itertools import permutations

consonants = 'РЖМДН'
vowels = 'ЕИО'
count = 0
for w in permutations(consonants + vowels, r=6):
    if w[0] in consonants and w[1] in vowels and w[-1] in vowels:
        count += 1
print(count)