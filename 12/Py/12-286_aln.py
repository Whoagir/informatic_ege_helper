# Автор: А.Л. Наймушин
# 12.286

for i in range(301,350):
  s = i*'8'
  while "555" in s or "888" in s:
    if "555" in s:
        s = s.replace( "555", "8", 1 )
    else:
        s = s.replace( "888", "55", 1 )
  if s.count('5')> s.count('8'):
    print (i, s)
    break
'''
Rez 304
'''
