from itertools import product

#------------------------------------------
known = {'А': '00', 'Б': '01', 'В': '110', 'Г': '101', 'Д': '100'}
#------------------------------------------

maxL = 4

def phanoOK( code, known ):
  return all( not c.startswith(code) and not code.startswith(c)
              for c in known.values() )

allCodes = [ ''.join(w) for i in range(1,maxL+1)
             for w in product('01', repeat=i) ]
allCodes = [ code for code in allCodes if phanoOK(code, known) ]

print( sorted(allCodes, key=len) )