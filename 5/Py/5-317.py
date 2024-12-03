# PRO100 ЕГЭ

for N in range(4, 100):
    N_2 = bin(N)[2:]
    if N % 4 == 0:
        r_2 = N_2 + N_2[-2:]
    else:
        ost_2 = bin(N % 4 * 2)[2:]
        r_2 = ost_2 + N_2

    if int(r_2, 2) < 68:
        print(N)





