# Михлин Б.С. Решение способом А. Кабанова.
# 1921.106

def f(s, c, m): # s - колич. камей в 1-й куче, c - счетчик ходов
    if s >= 165:
        return c % 2 == m % 2
    if c == m:
        return 0
    h = [f(s + 1, c + 1, m), f(s * 2, c + 1, m)]
    return any(h) if (c + 1) % 2 == m % 2 else all(h) # для № 19, 20, 21

for s in range(1, 165):
    for m in range(1, 5):
        if f(s, 0, m):
            print(s, m)  # Ответ: № 19: 82; № 20: 41, 81; № 21: 80
            break
'''
41 3 № 20
80 4 № 21
81 3 № 20
82 2 № 19
83 1
...
'''