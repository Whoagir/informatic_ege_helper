// Автор: Зубов Н.С.
program trisem;
uses crt;
var n,k,min:integer;
begin 
min:=7999;
k:=0;
for n:=3905 to 7998 do 
begin
if (((n mod 100) div 10<>0) and ((n mod 100) div 10<>5)) and (((n div 100) mod 10>=2)) and ((n div 100) mod 10<=6)
then
 begin
 k:=k+1;
 if min>n then min:=n;
 end;
 end;
 writeln(k,' ',min);
 end.
