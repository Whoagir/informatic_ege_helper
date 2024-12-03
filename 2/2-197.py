#----------------------------------------
template = '1**0 1001 *01*'.split()
val = 1

def f(x, y, z, w):
  f = (w <= z) and ((y <= x) == (z <= y))
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
tbCount = len(realTable)
pRealTable = list( permutations(range(tbCount)) )

for pCol in pColAll:
  for pTab in pRealTable:
    OK = True
    for i in range(rowCount):
      OK = OK and match(realTable[pTab[i]], pCol, template[i])
    if OK:
      print( "".join(['xyzw'[i] for i in pCol]) )
      break

