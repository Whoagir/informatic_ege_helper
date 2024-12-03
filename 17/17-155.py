# Автор В.Н. Шубинкин

with open('17-1.txt') as f:
    a = [int(x) for x in f.readlines()]

count = 0
mx = -20000
for i in range(1, len(a) - 1):
    if a[i - 1] > a[i] < a[i + 1]:
        count += 1
        mx = max(mx, a[i])
print(count, mx)
