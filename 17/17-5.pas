// Автор: Зубов Н.С.
program n10_2;
uses crt;
var n,k,max:integer;
begin
k:=0;
max:=1606;
for n:=1606 to 9680 do
    if (n mod 11 = 0) and (n mod 7>0) and (n mod 13>0) and (n mod 17>0) and (n mod 19>0)
    then begin
    k:=k+1;
     if n>max then
     max:=n;
    end;
    write(k,' ',max);
end.