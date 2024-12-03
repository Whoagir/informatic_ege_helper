# PRO100 ЕГЭ

otv = 0
for N in range(11, 1000):
    N_2 = bin(N)[2:]
    if N % 10 == 0:
        r_2 = N_2 + N_2[-4:]
    else:
        ost_2 = bin((N % 10)**2 // 2)[2:]
        r_2 = N_2 + ost_2

    if int(r_2, 2) < 680:
        otv += 1

print(otv)




