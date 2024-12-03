data = [int(s) for s in open('17-400.txt')]
N = len(data)

minEven = min( x for x in data if x % 2 == 0 )

def valid( tri ):
  last3 = [x for x in tri if abs(x) % 10 == 3]
  cond2 = [x for x in tri if x < minEven]
  return len(last3) == 2 and cond2

count = 0
elements = set()
for i in range(N - 2):
  chunk = data[i:i+3]
  if valid(chunk):
    count += 1
    elements |= set(chunk)

print( count, int(sum(elements)/len(elements)) )



