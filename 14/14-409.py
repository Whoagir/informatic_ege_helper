# Автор: Д. Статный

def f(a, n):
    return sum(a[::-1][i]*n**i for i in range(len(a)))

for x in range(67):
    a = f([3, x, 2, 1], 81) + f([1, 7, x, 4], 67)
    if a%35==0:
        print(x, a//35)