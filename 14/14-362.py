# Автор В.Н. Шубинкин

def dec(num, x):
    s = 0
    px = 1
    for d in num[::-1]:
        s += int(d) * px
        px *= x
    return s


count = 0   
for x in range(6, 80):
    x1 = dec('55113', x)
    x2 = dec('7005', 80) + x * 80**2 + x * 80
    res = x1 + x2
    count += abs(x1 - x2) <= 10**6
print(count)



