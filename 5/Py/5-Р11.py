def alg(x):
  s = "{:b}".format(x)
  return x - int( s[1:], 2 )

allResults = set()
for x in range(500, 5001):
  allResults.add(alg(x))

print(len(allResults))
