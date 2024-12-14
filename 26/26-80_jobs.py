# Автор: Е. Джобс

with open('26-80.txt') as f:
    n = int(f.readline())
    rows = {}
    for _ in range(n):
        a, b = map(int, f.readline().split())
        rows[a] = rows.get(a, set()) | {b}

    count = 0
    mc = mi = 0
    for r in sorted(rows.keys()):
        row = sorted(rows[r])
        c = 0
        if len(row) > 1:
            if row[1] - row[0] > 2:
                c += 1
                row[0] += 2
            for i in range(1, len(row) - 1):
                if not (row[i] - row[i-1] <= 2 or row[i+1] - row[i] <= 2):
                    c += 1
                    row[i] += 2
            if row[-1] - row[-2] > 2:
                c += 1
        else:
            c = 1
        count += c
        if mc < c:
            mc = c
            mi = r
    print(count, mi)
