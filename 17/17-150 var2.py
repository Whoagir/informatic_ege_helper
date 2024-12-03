# Автор В.Н. Шубинкин

count = 0
min_s = 20000
with open('17-1.txt') as f:
    a = int(f.readline())
    for line in f.readlines():
        b = int(line)
        if (a % 7 == 0 and b % 17 != 0
            or b % 7 == 0 and a % 17 != 0):
            count += 1
            min_s = min(min_s, a + b)
        a = b
print(count, min_s)
