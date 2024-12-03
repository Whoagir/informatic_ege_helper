// Автор: Зубов Н.С.
uses crt;
var max,min,n:integer;
begin
max:=0;
min:=8300;
for n:=3232 to 8299 do
if ((n mod 2 =0) or (n mod 7 =0)) and (n mod 15 <>0)  and (n mod 28<>0)
 and (n mod 41 <>0) then begin
 if max<n then
 max:=n;
 if min>n then
 min:=n;
 end;
 write(min,' ',max);
 end.