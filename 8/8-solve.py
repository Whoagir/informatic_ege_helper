def valid( word ):
  return word.count('К') == 1

def rec( word, k, Alpha ):
  if len(word) == k:
    if valid(word): return 1
    return 0
  count = 0
  for c in Alpha:
    count += rec( word+c, k, Alpha )
  return count

print( rec( "", 3, "ШКОЛА" ) )