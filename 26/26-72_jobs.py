# Авор: Е. Джобс

with open('26-72.txt') as f:
    n, m, k = map(int, f.readline().split())
    points = [tuple(map(int, s.split())) for s in f]
    points += [(i, 0) for i in range(1, m + 1)]
    points += [(i, n+1) for i in range(1, m + 1)]
    points.sort()
    res = {}
    for p1, p2 in zip(points, points[1:]):
        if p1[0] == p2[0]:
            if p2[1] - p1[1] >= 5:
                if p1[0] in res:
                    res[p1[0]] += p2[1] - p1[1] - 4
                else:
                    res[p1[0]] = p2[1] - p1[1] - 4
    s, mx = 0, list(res.keys())[0]
    for k in sorted(res.keys()):
        s += res[k]
        if res[mx] < res[k]:
            mx = k
    print(s, mx)

