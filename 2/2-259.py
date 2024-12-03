from itertools import *
from fnmatch import fnmatch

def f( x, y, z, w ):
  return not(x <= w) or (y <= z) or not y

templates = [ '?0??0', '01??0', '1??00' ]

tbl = [ list(xyzw) + [int(f(*xyzw))]
        for xyzw in product([0,1], repeat=4)]

def apply( s, p ):
  sp = [ s[p[i]] for i in range(4) ] + s[-1:]
  return ''.join( map(str, sp) )

for p in permutations(range(4)):
  tblp = [ apply(s, p) for s in tbl ]
  match = set( s for s in tblp
               if any( fnmatch(s,t) for t in templates ) )
  if len(match) == len(templates)  and \
     all( any(fnmatch(m,t) for m in match) for t in templates  ):
     print( ''.join('xyzw'[i] for i in p) )
