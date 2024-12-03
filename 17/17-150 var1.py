# Автор В.Н. Шубинкин

with open('17-1.txt') as f:
    a = [int(x) for x in f.readlines()]
count = 0
min_s = 20000
for i in range(len(a) - 1):
    if (a[i] % 7 == 0 and a[i + 1] % 17 != 0
        or a[i + 1] % 7 == 0 and a[i] % 17 != 0):
        count += 1
        min_s = min(min_s, a[i] + a[i + 1])
print(count, min_s)
