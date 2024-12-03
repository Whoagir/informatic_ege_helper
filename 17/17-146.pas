// Автор: С.П. Пуляшкина
##
uses school;

var z:=(25552..58885).Where(
     x ->x.Divisors.Where(y -> (y >9)and (y<100)).Count>14) ;
Print( z.Max, z.Count );


