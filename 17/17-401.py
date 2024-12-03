data = [int(s) for s in open('17-401.txt')]
N = len(data)

max7 = max( x for x in data if abs(x) % 10 == 7 )

def valid( tri ):
  odd = [x for x in tri if abs(x) % 2 == 1]
  cond2 = [x for x in tri if x > max7]
  return len(odd) == 2 and len(cond2) == 1

count = 0
elements = set()
for i in range(N - 2):
  chunk = data[i:i+3]
  if valid(chunk):
    count += 1
    elements |= set(chunk)

average = sum(elements)/len(elements)
print( count, str(average)[:3] )



