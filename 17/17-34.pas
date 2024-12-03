// Автор: Зубов Н.С.
program n_1;
uses crt;
var n, m, d, min, max:integer;
begin
max:=0;
min:=10000;
for n:= 1000 to 9999 do begin
m:=n;
d:=0;
while m>0 do begin
m:=m div 4;
d:=d+1;
end;
    if ((n mod 3<>0) and (n mod 17<>0) and (n mod 19<>0)) and (d=6) then begin
         if max<n then
        max:=n;
        if min>n then
            min:=n;

    end;
end;
writeln(min,' ',max);
end.