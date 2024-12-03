# Автор В.Н. Шубинкин

with open('17-1.txt') as f:
    a = [int(x) for x in f.readlines()]

max_len = 0
count = 0
k = 1
for i in range(1, len(a)):
    if a[i] < a[i - 1]:
        k += 1
        if k > max_len:
            max_len = k
            count = 0
        if k == max_len:
            count += 1
    else:
        k = 1
print(max_len, count)
