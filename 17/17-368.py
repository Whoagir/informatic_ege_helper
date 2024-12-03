data = [int(s) for s in open('17-354.txt')]

avgXX = [x for x in data if abs(x) % 10 == (abs(x) % 100) // 10]
avgXX = sum(avgXX) / len(avgXX)

result = []
for a, b in zip(data, data[1:]):
  if (abs(a) % 10 == abs(b) % 100 // 10 or
      abs(b) % 10 == abs(a) % 100 // 10) and \
     ((a % 11 == 0) ^ (b % 11 == 0)) and \
     a*a + b*b >= avgXX*avgXX:
     result.append( a*a + b*b )

print( len(result), max(result) )
