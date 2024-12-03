# Автор В.Н. Шубинкин

def control_sum(num):
    s = 0
    while num:
        s += num % 10
        num //= 10
        d = 2 * (num % 10)
        d = d % 10 + d // 10
        s += d
        num //= 10
    return s


num = 1000_0000_0000_0000
num += 1
while control_sum(num) != 25:
    num += 1
print(num, num % 10**15)
