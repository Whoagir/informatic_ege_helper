from itertools import combinations

A = '0369'
dayVar = list( combinations(A, 2) ) + \
         list( combinations(A, 3) ) + \
         list( combinations(A, 4) )

count = 0
for d1 in dayVar:
  for d2 in dayVar:
    for d3 in dayVar:
      s = d1 + d2 + d3
      if s.count('3') > 1:
        count += 1

print( count )

