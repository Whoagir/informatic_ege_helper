from itertools import product

allWords = set()
for x in product('POLYGON', repeat=5):
  s = ''.join(x)
  if s == s[::-1] and s[2] in 'OY':
    allWords.add(s)

print( len(allWords) )
