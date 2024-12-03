# Автор: Д. Статный

def cc(x):
    mx = max([int(str(i), 36) for i in x])
    a = [int(str(i), 36) for i in str(x)]
    return sum(int(a[::-1][i])*(mx+1)**i for i in range(len(a)))

a = [x.strip() for x in open('17-362.txt')]
ans = []
for i in range(len(a)-1):
    mxi = max([int(str(i), 36) for i in a[i]])
    mxj = max([int(str(i), 36) for i in a[i+1]])
    if abs(mxi-mxj)<=2:
        ans.append(cc(a[i])+cc(a[i+1]))
print(len(ans), max(ans))