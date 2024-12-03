# PRO100 ЕГЭ

a = []
for N in range(4, 100):
    N_2 = bin(N)[2:]
    if N % 3 == 0:
        r_2 = N_2 + N_2[-3:]
    else:
        ost_2 = bin(N % 3 * 3)[2:]
        r_2 = N_2 + ost_2

    R = int(r_2, 2)
    if R < 68:
        a.append(R)

print(max(a))