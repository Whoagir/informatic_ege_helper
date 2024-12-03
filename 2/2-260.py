from itertools import *
from fnmatch import fnmatch

def f1( x, y, z, w ):
  return (w <= z) == (y <= x)

def f2( x, y, z, w ):
  return (w <= z) and ((not x) == y)

templates = [ '?0000?', '?011?0', '00?001' ]

tbl = [ list(xyzw) + [int(f1(*xyzw)), int(f2(*xyzw))]
        for xyzw in product([0,1], repeat=4)]

def apply( s, p ):
  sp = [ s[p[i]] for i in range(4) ] + s[4:]
  return ''.join( map(str, sp) )

for p in permutations(range(4)):
  tblp = [ apply(s, p) for s in tbl ]
  match = set( s for s in tblp
               if any( fnmatch(s,t) for t in templates ) )
  if len(match) >= len(templates)  and \
     all( any(fnmatch(m,t) for m in match) for t in templates  ):
     print( ''.join('xyzw'[i] for i in p) )
