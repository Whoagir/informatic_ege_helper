# Автор В.Н. Шубинкин

with open('17-1.txt') as f:
    a = [int(x) for x in f.readlines()]

count = 0
min_el = 20000
for i in range(len(a) - 1):
    if (abs(a[i]) % 10 == 6 and a[i] % 3 == 0
        or abs(a[i + 1]) % 10 == 6 and a[i + 1] % 3 == 0):
        count += 1
        min_el = min(min_el, a[i], a[i + 1])
print(count, min_el)

