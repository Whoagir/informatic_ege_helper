# Автор: Л. Шастин

with open('26-68.txt') as f:

    N, T = map(int, f.readline().split())
    V = [list(map(int, f.readline().split())) for j in range(N)]

    # делим все вирусы на две группы по уровню. опасности
    M = sum(x[0] for x in V)/N    # средний уровень опасности
    vSuper = sorted(x[1] for x in V if x[0] > M) # супервирусы
    vWeak = sorted(x[1] for x in V if x[0] < M) # обычные

    count, timeAll, timeSuper =  0, 0, 0
    for i in range(len(vWeak)):
        if i < len(vSuper) and timeAll + vWeak[i] + vSuper[i] <= T:
            timeAll += (vWeak[i] + vSuper[i])
            timeSuper += vSuper[i]
            count += 2
        elif timeAll + vWeak[i] <= T:
            timeAll += vWeak[i]
            count += 1

    print( count, timeSuper )

