// Автор: Зубов Н.С.
var k,n:integer;
function F( n: integer ): integer;
begin
  if n <=3 then F:= n
else
  if (n>3) and (n mod 2=0) then F := n + 3+F(n-1)
else
   F := n*n + F(n-2);
end;
begin
  k:=0;
  for n:=1 to 1000 do 
    if F(n) mod 7 =0 then begin
      k:=k+1;
    end;
  writeln(k);
end.