// Автор: Зубов Н.С.
program n10;
uses crt;
var n,k,min:integer;
begin
k:=0;
min:=9504;
for n:=1107 to 9504 do
    if (n mod 9 =0) and (n mod 7<>0) and (n mod 15<>0) and (n mod 17<>0) and (n mod 19<>0)
    then begin
    k:=k+1;
     if n<min then
     min:=n;
    end;
    write(k,' ',min);
end.