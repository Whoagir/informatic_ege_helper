from itertools import product

#------------------------------------------
known = 'А11 Б0110 В001'
wordToCode = 'СТРАТОСТАТ'
alphabet = set(wordToCode) | set('.')
#------------------------------------------

maxL = 4

def encode( word, dic ):
  return ''.join( [ dic[c] for c in word ] )

def phanoOK( code, known ):
  return all( not c.startswith(code) and not code.startswith(c)
              for c in known.values() )

known = { s[0]: s[1:] for s in known.split() }
unknown = list( alphabet - set(known) )

allCodes = [ ''.join(w) for i in range(1,maxL+1)
             for w in product('01', repeat=i) ]
allCodes = [ code for code in allCodes if phanoOK(code, known) ]

minLen = 100
def tryCode( unknown, known, freeCodes ):
  global minLen
  if not unknown:
    coded = encode( wordToCode, known )
    if len(coded) <= minLen:
      minLen = len(coded)
      print( coded, minLen, known )
    return
  for i, c in enumerate(freeCodes):
    if phanoOK( c, known ):
      tryCode( unknown[1:], known | {unknown[0]: c },
               freeCodes[:i]+freeCodes[i+1:] )

tryCode( unknown, known, allCodes )

