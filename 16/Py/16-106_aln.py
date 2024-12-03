#106_Автор задачи А.Л.Наймушин	
def F( n ):
  if n == 0: return 3
  elif 0<n <= 15: return F(n-1)
  elif 15<n < 95: return 2.5*F(n-3)
  
  else:
      if n >= 95:
        return 3.3* F(n-2)
print(F(70) )
      
otv = int(F(70))
print( otv)
s = str(otv)
print('Ответ: ',s[0])

           

'''
109139364.21275139
109139364
Ответ: 1

'''



