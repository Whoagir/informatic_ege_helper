A = "КАБАЛА"

no = [ "АА" ]

def valid( word ):
  for ex in no:
    if ex in word:
      return False
  return True

allWords = []
def rec( word, k, Alpha ):
  if len(word) == k:
    if valid(word) and not word in allWords:
      allWords.append( word )
      return 1
    return 0
  count = 0
  m = len(word)
  Alpha = list(Alpha)
  for i in range(m,len(Alpha)):
    Alpha[i], Alpha[m] = Alpha[m], Alpha[i]
    count += rec( word+Alpha[m], k, Alpha )
    Alpha[i], Alpha[m] = Alpha[m], Alpha[i]
  return count

print( rec( "", len(A), A ) )
