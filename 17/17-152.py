# Автор В.Н. Шубинкин


with open('17-1.txt') as f:
    a = [int(x) for x in f.readlines()]

count = 0
max_el = -20000
for i in range(len(a) - 1):
    if ((a[i] % 9 == 0 and a[i + 1] % 9 != 0 and abs(a[i + 1]) % 8 == 3)
        or (a[i + 1] % 9 == 0 and a[i] % 9 != 0 and abs(a[i]) % 8 == 3)):
        count += 1
        max_el = max(max_el, a[i], a[i + 1])
print(count, max_el)
