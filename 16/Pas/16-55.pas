// Автор: Зубов Н.С.
var k,n:integer;
function F( n: integer ): integer;
begin
  if n >25 then F:= 2*n*n*n+1
else
  if n<=25 then F := F(n+2) + 2*F(n+3)
end;
begin
  k:=0;
  for n:=1 to 1000 do 
    if F(n) mod 11 =0 then begin
      k:=k+1;
    end;
  writeln(k);
end.