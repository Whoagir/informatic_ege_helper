# PRO100 ЕГЭ

for N in range(3, 100):
    N_2 = bin(N)[2:]
    if N % 3 == 0:
        r_2 = N_2 + N_2[-3:]
    else:
        ost_2 = bin(N % 3 * 3)[2:]
        r_2 = N_2 + ost_2

    if int(r_2, 2) >= 120:
        print(N)
        break