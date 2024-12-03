# Автор: А. Куканова

from itertools import permutations

count = 0
consonants = 'ДЙКСТР'
vowels = 'ЕА'
words = ("".join(w) for w in permutations(consonants + vowels, r=6))
for w in words:
    if w.count('Й') == 1 and any('Й' + char in w for char in consonants):
        count += 1
print(count)