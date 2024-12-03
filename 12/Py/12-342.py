# Автор: Е. Джобс

for n in range(108, 250, 9):
    s = '5'*n
    while '555' in s or '11' in s or '2' in s:
        s = s.replace('555', '1', 1)
        s = s.replace('11', '25', 1)
        s = s.replace('2', '5', 1)
    print(n, s)
