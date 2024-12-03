# Автор: А. Куканова

from itertools import product

words = [''.join(w) for w in product('СОЛНЦЕ', repeat=6)]
words = [w for w in words if w.count('О') <= 2 and w.count('Ц') == 1]
print(len(words))
