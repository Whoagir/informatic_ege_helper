# Автор: Л. Шастин

f = open('26-135.txt')
n = int(f.readline())
rows = sorted(list(map(int, f.readline().split())) for i in range(n))
count = 0
for i in range(len(rows) - 2):
    if rows[i + 2][0] == rows[i][0] and \
            rows[i + 1][1] - rows[i][1] == 6 and rows[i + 2][1] - rows[i + 1][1] == 6:
        count += 1
        mr = rows[i][0]
print(mr, count)

