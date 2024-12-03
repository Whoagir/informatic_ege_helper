#----------------------------------------
template = '0001 1110'.split()
val = 0

def f(x, y, z, w):
  f = (x == y) <= (z == w)
  return int(f > 0)
#----------------------------------------

def tbIst( f, val ):
  res = []
  for x in range(2):
    for y in range(2):
      for z in range(2):
        for w in range(2):
          if f(x, y, z, w) == val:
            res.append( "{}{}{}{}".format(x, y, z, w))
  return res

def match( s, p, template ):
  if len(s) != len(template): return False
  res = True
  for i in range(len(s)):
    res = res and (template[i] == '*'  or  s[p[i]] == template[i])
  return res

from itertools import permutations

colCount = len(template[0])
rowCount = len(template)
pColAll = list( permutations(range(colCount)) )

realTable = tbIst(f, val)
realTable = [x for x in realTable
               if x.count('1') == 3 or x.count('1') == 1 ]

tbCount = len(realTable)
pRealTable = list( permutations(range(tbCount)) )

count = 0
for pCol in pColAll:
  for pTab in pRealTable:
    OK = True
    for i in range(rowCount):
      OK = OK and match(realTable[pTab[i]], pCol, template[i])
    if OK:
      print( "".join(['xyzw'[i] for i in pCol]) )
      count += 1
      break

print( count )