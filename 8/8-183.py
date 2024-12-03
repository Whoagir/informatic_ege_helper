A = "0123456789ABCDEF"
N = 15

A = list( reversed(A) )
Aeven = [x for x in A if ord(x) % 2 == 0]
Aodd = [x for x in A if ord(x) % 2 != 0]

allWords = []

def rec( word, k, Alpha ):
  #print( ' '*len(word), '>'+word+'<', k, Alpha )
  if len(word) == k:
    if not word in allWords:
      allWords.append( word )
      return 1
    return 0
  count = 0
  for i, c in enumerate(Alpha):
    if( word == '' or
        (
        (Alpha.index(c) % 2 != Alpha.index(word[-1]) % 2) and
        (Alpha.index(c) > Alpha.index(word[-1]))
        )
        ):
      count += rec( word+c, k, Alpha )
  return count

print( rec( "", N, A ) )
