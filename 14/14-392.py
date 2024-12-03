# Автор: И. Карпачев

def dec(arr, q):
    arr = arr[::-1]
    s = 0
    for i in range(len(arr)):
        s += arr[i] * q ** i
    return s

for x in range(17):
    v = dec([3, 11, 8, x, 1], 17) + dec([2, x, 9, x, 3], 17)
    a = v
    s = 0
    while a != 0:
        if a % 6 == 5:
            s = s + 1
        a = a // 6
    if s == 3:
        print(x, v)

