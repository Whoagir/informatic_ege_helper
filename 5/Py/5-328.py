# Автор: Е. Джобс

res = set()
for N in range(1, 223):
    b = bin(N)[2:]
    if N % 5 == 0:
        b = '1' + b + b[-2:]
    else:
        b = bin(N%5)[2:] + b
    R = int(b, 2)
    if R <= 223:
        res.add(R)
print(max(res))
