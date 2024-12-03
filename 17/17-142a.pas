// Автор: С.П. Пуляшкина
##
uses school;

var z:=(1412..7865).Where(
       x ->(x.Divs(8) or x.Divs(19))and x.NotDivs(4) and x.NotDivs(9) 
            and x.Digits.Sum.NotDivs(5));
print( z.min, z.max );


