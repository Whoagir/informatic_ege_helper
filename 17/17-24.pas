// Автор: Зубов Н.С.
program n10_2;
uses crt;
var n,max,min:integer;
begin
max:=7858;
min:=2568;
for n:=2568 to 7858 do
    if ((n mod 4 = 0) or (n mod 5 = 0)) and (n mod 11>0) and (n mod 20>0) and (n mod 27>0)
    then begin
     if n>min then
     max:=n;
     if n<max then
     min:=n;
    end;
    write(min,' ',max);
end.