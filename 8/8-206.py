# Автор: А. Куканова

from itertools import product

vowels = 'ЯОИЕ'
consonants = 'СНВДЦ'

count = 0
for w in product(vowels + consonants, repeat=5):
    if (w[0] in consonants and w.count(w[0]) == 1
            and w[-1] in vowels and w.count(w[-1]) == 1):
        count += 1
print(count)