// Автор: Зубов Н.С.
program n10_2;
uses crt;
var n,k,max:integer;
begin
k:=0;
max:=12567;
for n:=1390 to 12567 do
    if ((n mod 3 = 0) or (n mod 5 = 0)) and (n mod 7>0) and (n mod 11>0) and (n mod 13>0) and (n mod 23>0)
    then begin
    k:=k+1;
     if n>max then
     max:=n;
    end;
    write(k,' ',max);
end.