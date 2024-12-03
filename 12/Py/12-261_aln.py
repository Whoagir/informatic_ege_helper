# Автор: А.Л. Наймушин
# 12.261

s = 52*'AB'
while "AA" in s or "BB" in s or "AB" in s:
  if "AA" in s:
    s = s.replace( "AA", "B", 1 )
  elif "BB" in s:
    s = s.replace( "BB", "A", 1 )
  elif "AB" in s:
    s = s.replace( "AB", "BA", 1 )

print(s)

# Ответ: ВА

