// Автор: С.П. Пуляшкина
##
uses school;

var z:=(3399..225599).Where(
    x->(ToBase(x,5).Right(1)='3') 
       and (ToBase(x,7).CountOf('0')=0));
Print( z.count, z.max );
