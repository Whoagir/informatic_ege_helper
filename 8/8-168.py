A = "КЛЕЙ"
N = 6
no = [ ".Й", "ЕЙ", "ЙЕ", "Й." ]

def valid( word ):
  word = '.' + word + '.'
  if word.count("Й") > 1:
    return False
  for ex in no:
    if ex in word:
      return False
  return True

def rec( word, k, Alpha ):
  if len(word) == k:
    if valid(word): return 1
    return 0
  count = 0
  for c in Alpha:
    count += rec( word+c, k, Alpha )
  return count

print( rec( "", N, A ) )
