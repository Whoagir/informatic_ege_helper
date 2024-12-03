// Автор: С.П. Пуляшкина
##
uses school;
var z:=(2848..109499).Where(
   x ->(9 in x.Digits) and 
       (x.Digits.Where(y ->y>5).Sum).Divs(3));
var v := z.Where(x ->x.Digits.First = 8).Max.Print;
print( z.count )
