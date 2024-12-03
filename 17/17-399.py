data = [int(s) for s in open('17-399.txt')]

min5 = min( x for x in data
              if 100 <= abs(x) <= 999 and abs(x) // 100 == 5 )

results = []
for a, b in zip(data, data[1:]):
  if (abs(a)%10 == 4) != (abs(b)%10 == 4) and (a+b) % min5 != 0:
    results.append( a + b )

print( len(results), max(results) )