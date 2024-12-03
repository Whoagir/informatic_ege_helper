# Автор В.Н. Шубинкин

with open('17-1.txt') as f:
    a = [int(x) for x in f.readlines()]

count = 0
min_dist = 20000
pos = -1
for i in range(1, len(a) - 1):
    if a[i - 1] < a[i] > a[i + 1]:
        count += 1
        if pos != -1:
            min_dist = min(min_dist, i - pos)
        pos = i
print(count, min_dist)
