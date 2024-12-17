c = 0
for n in range(11, 1000):
    s = bin(n)[2:]
    v = str(s)[-4::]
    # Последние 4 цифры в обратном порядке
    d = str(n)[-1]  # Последняя цифра числа n
    d1 = (int(d) ** 2) // 2  # Последняя цифра в квадрате, разделенная на 2
    # print(n,s,v,d,d1)
    if int(n) % 10 == 0:
        s1 = str(s) +v
        # print (s,s1)
    else:
        s1 = s + bin(d1)[2:]
    # print(s,s1)
    r = int(s1, 2)
    if r < 680:
        c += 1
print(c)