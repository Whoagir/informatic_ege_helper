# Автор: И. Карпачев

def dec(arr, q):
    arr = arr[::-1]
    s = 0
    for i in range(len(arr)):
        s += arr[i] * q ** i
    return s

for x in range(8):
    v = dec([5, 7, 10, x, 9], 16) * dec([5, 4, x], 8)
    a = v
    s = 0
    while a != 0:
        s = s + a % 12
        a = a // 12
    if s == 40:
        print(x, v)
