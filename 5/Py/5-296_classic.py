# Автор В.Н. Шубинкин

def is_correct(num):
    s = 0
    while num:
        s += num % 10
        num //= 10
        d = 2 * (num % 10)
        d = d % 10 + d // 10
        s += d
        num //= 10
    return s % 10 == 0


num = 1234_5678_9101_1121
num += 1
while not is_correct(num):
    num += 1
print(num % 10**8)
