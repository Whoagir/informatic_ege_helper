data = [int(s) for s in open('17-410.txt')]
N = len(data)

M = min(data)

results = []
for i in range(N-1):
  if M in [data[i] % 16, data[i+1] % 16]:
    results.append( sum(data[i:i+2]) )

print( len(results), max(results) )



