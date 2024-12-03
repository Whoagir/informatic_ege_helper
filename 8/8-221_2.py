# Михлин Б.С.
'''
8.221_2 (А. Куканова) Лиза составляет слова из букв О, Н, И, К, С, причём буква С должна встречаться в этих словах ровно 3 раза,
а буква О — ровно 1 раз. Длина слова составляет от 4 до 6 букв.
Сколько различных слов может составить Лиза?
'''
from itertools import product
w4 = [p for p in product('оникс', repeat=4) if ''.join(p).count('с') == 3 and ''.join(p).count('о') == 1]
w5 = [p for p in product('оникс', repeat=5) if ''.join(p).count('с') == 3 and ''.join(p).count('о') == 1]
w6 = [p for p in product('оникс', repeat=6) if ''.join(p).count('с') == 3 and ''.join(p).count('о') == 1]
print(len(w4 + w5 + w6))  # print(len(w4) + len(w5) + len(w6))  # Ответ: 604