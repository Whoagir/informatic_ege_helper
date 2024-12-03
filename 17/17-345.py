# Автор: М. Ишимов

a = [int(x) for x in open('17-345.txt')]
end = [x for x in a if x % 100 == 52]
res = []
dif = max(end) - min(end)

for i in range(len(a) - 1):
    if (a[i] < dif) + (a[i+1] < dif) == 1: res.append(a[i] + a[i+1])

print(len(res), max(res))