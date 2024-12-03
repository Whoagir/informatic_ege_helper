# PRO100 ЕГЭ

for N in range(4, 100):
    N_2 = bin(N)[2:]
    if N % 5 == 0:
        r_2 = N_2 + N_2[-3:]
    else:
        ost_2 = bin(N % 5 * 5)[2:]
        r_2 = N_2 + ost_2

    if int(r_2, 2) < 100:
        print(N)



