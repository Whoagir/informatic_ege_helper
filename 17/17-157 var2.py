# Автор В.Н. Шубинкин

mn = 20000
count = 0
pos = -1
with open('17-2.txt') as f:
    for i, line in enumerate(f.readlines(), 1):
        a = int(line)
        if a < mn:
            mn = a
            count = 0
        if a == mn:
            count += 1
            pos = i
print(count, pos)
