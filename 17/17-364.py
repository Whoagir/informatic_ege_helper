# Автор: Н. Сафронов

s = list(map(int, open('17-363.txt')))
m = max(x for x in s if len([i for i in str(x) if i in '02468']) == len([i for i in str(x) if i in '13579']))
r = []
for i in range(len(s) - 1):
    if all(x > y for x in str(s[i]) for y in str(s[i + 1])):
        if s[i] + s[i + 1] <= m:
            r.append(s[i] + s[i + 1])
print(len(r), max(r))
