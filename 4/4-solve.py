from collections import Counter

fixed = { 'Б': '01', 'В': '001', 'Е': '0001', 'Ш': '111' }
word = 'КУКУШКА'

fixed = { 'А': '000', 'Б': '0010', 'В': '101', 'Г': '11' }
word = 'КОЛОБОК'

def genAllCodes( start, k ):
  r = k - len(start)
  n = 2**r
  allCodes = []
  for i in range(n):
    code = (start+bin(i)[2:]).zfill(k)
    allCodes.append( code )
  return allCodes

def phano( code, busyCodes ):
  for oldCode in busyCodes:
    if oldCode.startswith( code ):
      return False
    if code.startswith( oldCode ):
      return False
  return True

def freeBinCodes():
  busyCodes = list(fixed.values())
  freeCodes = []
  for k in range(1,4):
    kCodes = genAllCodes( '', k )
    for code in kCodes:
      if phano( code, busyCodes ):
        if phano( code, freeCodes ):
          freeCodes.append( code )
          busyCodes.append( code )
  return freeCodes

def unknown( s ):
  letters = []
  for c in s:
    if not c in fixed:
      letters.append( c )
  return letters

cntWord = Counter( unknown(word) )
cntWord['.'] = 0 # остальные буквы
print( cntWord )
letters = [ k for k, v in cntWord.most_common()]

available = freeBinCodes()
print( available )

def lenOfCode( avl ):
  n = 0
  for c in word:
    if c in fixed:
      n += len(fixed[c])
    else:
      pos = letters.index(c)
      n += len(avl[pos])
  return n

minLen = 1e10
def recTest( changeFrom ):
  global minLen
  avl = available[:]
  print( avl, changeFrom )
  i = changeFrom
  while len(avl) < len(letters):
    if i >= len(avl):
      i -= 2
    avl.insert( i+1, avl[i]+'1' )
    avl[i] += '0'
    print( avl )
    i += 2
  avl.sort( key=len )
  print( avl )
  curLen = lenOfCode( avl )
  if curLen <= minLen:
    minLen = curLen
  print( curLen )

for k in range(len(available)):
  print( "k =", k )
  recTest( k )

print( 'Ответ:', minLen )

























