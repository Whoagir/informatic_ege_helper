# Автор: Н. Сафронов

s = list(map(int, open('17-363.txt')))
m = max(x for x in s if all(i in '13579' for i in str(x)))
r = []
for i in range(len(s) - 1):
    if all(x in '02468' for x in str(s[i])) or all(x in '02468' for x in str(s[i + 1])):
        if s[i] + s[i + 1] > m:
            r.append(s[i] + s[i + 1])
print(len(r), max(r))
