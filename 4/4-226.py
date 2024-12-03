d = {}
def phano( codes):
  full = list(codes.items())
  for i, p in full:
    for j, q in full:
      if i != j and p.startswith(q):
        return False
  return True

def hasFreeBranch( codes ):
  for i in range(1,6):
    for n in range(2**i):
      s = "{:0" + str(i) + "b}"
      s = s.format(n)
      if phano( codes | {'X': s}):
        #print( 'Free: ', s )
        return s
  return None

def decode( codes, word, tail ):
  global d
  if not phano(codes):
    return
  if not tail:
    if word: return
    print( codes )
#    if hasFreeBranch( codes ):
    d = codes
    return
  else:
    if not word: return
  if word[0] in codes:
    c = codes[word[0]]
    if tail.startswith(c):
      decode( codes, word[1:], tail[len(c):] )
  else:
    for i in range(1,len(tail)-len(word)+2):
      decode( codes | {word[0]: tail[:i]},
              word[1:], tail[i:] )

word = 'КРЕЧЕТ'
encoded = '110111100110001'
word1 = 'ЧЕК'

decode( {}, word, encoded )

free = hasFreeBranch( d )
if free:
  print( 'Free: ', free )
else:
  print( 'Нет свободных веток!')

print( word1, end=": ")
for c in word1:
  print( d[c], end='' )
print()



