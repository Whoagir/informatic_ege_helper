# Автор: И. Кушнир

a = [int(i) for i in open("17-336.txt")]
m8 = min( [i for i in a if i%8==0 and i!=8] )

m = 10**10
k = 0
mx = 0
for i in range(len(a)-1):
    if a[i] % m8 == 0 and a[i+1] % m8 == 0:
        k += 1
        if a[i] + a[i+1] < m:
            m = a[i] + a[i+1]
            mx = max( a[i], a[i+1] )
print( k, mx )
