# Автор: И. Карпачев

def dec(arr, q):
    arr = arr[::-1]
    s = 0
    for i in range(len(arr)):
        s += arr[i] * q ** i
    return s

M = int('M', 36)
F = int('F', 36)
T = int('T', 36)
Y = int('Y', 36)

for x in range(37):
    v = dec([M, F, x, 7, 2], 37) + dec([T, x, 7, Y, 2], 37)
    if v % 536 == 0:
        print(x, v // 536)
