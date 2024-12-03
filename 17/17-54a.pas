// Автор: С.П. Пуляшкина
##
uses school;
var a:= (2595..8401).Where( x -> x.Divs(2) and x.NotDivs(13) );
Println( a.Count, a.Sum )