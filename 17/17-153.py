# Автор В.Н. Шубинкин

with open('17-1.txt') as f:
    a = [int(x) for x in f.readlines()]

count = 0
min_r = 20000
for i in range(len(a) - 1):
    if a[i + 1] > a[i]:
        count += 1
        min_r = min(min_r, a[i + 1] - a[i])
print(count, min_r)
