# Автор: Е. Джобс

s = []
for x in '0123456789ABCDEF':
    for y in '0123456789ABCDEF':
        c1 = int(f'27A{x}23', 16)
        c2 = int(f'8{y}E5D2', 16)
        if (c1 + c2) % 5 == 0:
            s.append(int(x,16) + int(y,16))
print(max(s))
