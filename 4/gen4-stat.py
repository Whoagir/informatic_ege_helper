from random import shuffle
from collections import Counter

code2 = [ "{:02b}".format(x) for x in range(4) ]
code3 = [ "{:03b}".format(x) for x in range(8) ]

w1 = 'КАЧОК'
w2 = 'КОК'
syms = list(set(list(w1)))
c = Counter(w1)
freqSym = c.most_common(1)[0][0]

shuffle( code2 )
shuffle( code3 )
print( code2 )
print( code3 )
d = { freqSym: code2[0] }
code3 = [ x for x in code3 if not x.startswith(code2[0]) ]
for c in syms:
  if c != freqSym:
    d[c] = code3[0]
    del code3[0]

def encode( s, d ):
  code = ""
  for c in s:
    code += d[c]
  return code

print( d )
print( w1, encode(w1, d) )
print( w2, encode(w2, d) )


