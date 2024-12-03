# Автор: И. Кушнир

a = [ int(i) for i in open("17-336.txt") ]
m37 = max( [ i for i in a if i%37==0 ] )

mas = []
for i in range(len(a)-1):
    if (a[i] % m37 == 0 or a[i+1] % m37 ==0) and \
       (a[i] + a[i+1]) % m37 > 30:
        mas.append( a[i] + a[i+1] )
print( len(mas), min(mas) )
