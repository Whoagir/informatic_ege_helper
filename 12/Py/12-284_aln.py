# Автор: А.Л. Наймушин
# 12.284

for i in range(201,250):
  s = i*'8'
  while "555" in s or "888" in s:
    if "555" in s:
        s = s.replace( "555", "8", 1 )
    else:
        s = s.replace( "888", "55", 1 )
  if s.count('8') == s.count ('5'):
    print (i, s)
    break
'''
Rez 201 5588
'''
