# Автор В.Н. Шубинкин

def dec(num, x):
    s = 0
    px = 1
    for d in num[::-1]:
        s += int(d) * px
        px *= x
    return s


count = 0   
for x in range(6, 100):
    x1 = dec('13152', x)
    x2 = dec('7025', 100) + x * 100**2
    res = x1 + x2
    count += res % 11 == 0
print(count)



