# Автор: Н. Сафронов

def sd(n):
    return sum(map(int, str(n)))

s = [int(x) for x in open('17-385.txt')]
mins = sorted([[sd(abs(x)), x] for x in s], key=lambda p:(p[0], -p[1]))[0][1]
print(mins)

a = []
for i in range(len(s) - 1):
    if s[i] > mins and s[i + 1] > mins:
        a.append(sd(s[i]) + sd(s[i + 1]))
print(len(a), max(a))

