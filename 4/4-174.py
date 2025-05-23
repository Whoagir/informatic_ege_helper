dSave = {}
d = {}
def phano():
  dl = list(d.values())
  for i in range(len(dl)):
    for j in range(len(dl)):
      if i != j and dl[i].startswith(dl[j]):
        return False
  return True

def buildDict( word, code ):
  #print( word, code, d )
  if not word:
    if not code and all( 2<=len(x)<=3 for x in d.values() ):
      print('***', d)
      global dSave
      dSave = d.copy()
      return True
    else:
      return False
  if len(code) < 2: return False
  c = word[0]
  if c in d:
    code1 = d[c]
    m = len(code1)
    if code.startswith(code1):
      buildDict( word[1:], code[m:] )
    return
  d[c] = code[:2]
  if phano():
    buildDict( word[1:], code[2:] )
  del d[c]
  if len(code) < 3: return False
  d[c] = code[:3]
  if phano():
    buildDict( word[1:], code[3:] )
  del d[c]
  if len(code) < 4: return False
  d[c] = code[:4]
  if phano():
    buildDict( word[1:], code[4:] )
  del d[c]

def encode( s, d ):
  code = ""
  for c in s:
    code += d[c]
  return code

w1 = "МОЛОТ"
w2 = "ТОМ"
code = '1010010000011'
buildDict( w1, code )
print( encode(w2, dSave) )

