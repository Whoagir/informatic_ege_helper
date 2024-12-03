a = [int(x) for x in open('17-1.txt')]

def valid( x ):
  return abs(x) % 10 == 6 and abs(x) % 3 == 0

count = 0
mi = 20000
for i in range(len(a) - 1):
  if valid(a[i]) or valid(a[i+1]):
    count += 1
    mi = min(mi, a[i], a[i + 1])
print(count, mi)
