// Автор: С.П. Пуляшкина
##
uses school;

var z:=(2495..7083); 
z.Where(x->((Hex(x).Right(2)='1A') or (Hex(x).Right(2)='1F'))and 
      x.NotDivs(9) and x.NotDivs(5)).Count.Print;     
z.Where(x->((Hex(x).Right(2)='1A') or (Hex(x).Right(2)='1F'))and 
      x.NotDivs(9) and x.NotDivs(5)).Min.Println