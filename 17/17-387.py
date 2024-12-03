# Автор: PRO100-ЕГЭ

data = [ int(s) for s in open("17-387.txt") ]

N = len(data)

results = []
for i in range(N-3):
  if (abs(data[i]) % 100 == 13) != (abs(data[i+3]) % 100 == 13):
    results.append( data[i]+data[i+3] )

print( len(results), max(results) )
