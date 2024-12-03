# Автор: Д. Статный

s = '2222' + 38*'1' + '32'*30
while '33' in s or '22' in s or '11' in s:
  s = s.replace( '33', '12', 1 )
  s = s.replace( '11', '32', 1 )
  s = s.replace( '22', '31', 1 )

print( sum( map(int, s) ) )
