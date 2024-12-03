// Автор: Зубов Н.С.
program n_1;
uses crt;
var n,k,min,max:integer;sa:real;
begin
k:=0;
min:=7040;
max:=0;
for n:= 1476 to 7039 do begin
    if ((n mod 2=0) and (n mod 16<>0)) and (n div 10 mod 10 >=4) then begin
        inc(k);
        if n<min then
        min:=n;
        if n>max then
        max:=n;
    end;
end;
  sa:=(min+max)div 2;
  writeln(k,'  ',sa);
end.