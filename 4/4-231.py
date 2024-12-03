from itertools import product
#------------------------------------------
known = {'Ф': '00', 'С': '10', 'О': '11'}
#------------------------------------------
maxL = 4
def phanoOK( code, known ):
  return all( not c.startswith(code) and not code.startswith(c)
              for c in known.values() )
# переход к обратным кодам
known = { c: code[::-1] for c, code in known.items() }
allCodes = [ ''.join(w) for i in range(1,maxL+1)
             for w in product('01', repeat=i) ]
allCodes = [ code for code in allCodes if phanoOK(code, known) ]
# возврат к прямым кодам
print( sorted( [code[::-1] for code in allCodes], key=len) )