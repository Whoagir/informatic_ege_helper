# Автор В.Н. Шубинкин

mx = -20000
count = 0
pos = -1
with open('17-2.txt') as f:
    for i, line in enumerate(f.readlines(), 1):
        a = int(line)
        if a > mx:
            mx = a
            pos = i
            count = 0
        if a == mx:
            count += 1
print(count, pos)
            
