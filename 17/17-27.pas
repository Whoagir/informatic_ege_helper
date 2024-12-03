program n_27;
uses crt;
var n,k,max:integer;
begin
max:=8433;
k:=0;
for n:=3712 to 8432 do
if (n mod 2=n mod 4)and (((n mod 13=0) or (n mod 14=0)) or (n mod 15=0)) then begin
k:=k+1;
if (n<max) then
max:=n;
end;
writeln(k,' ',max);
end.

