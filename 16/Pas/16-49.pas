// Автор: Зубов Н.С.
var k,n,x:integer;
function F( n: integer ): integer;
begin
  if n <=3 then begin
    Result := n;
    Exit;
  end;
  if (n>3) and (n mod 2=0) then
    Result := 2*n + F(n-1)
  else
    Result := n*n + F(n-2);
end;
begin
  k:=0;
  for n:=1 to 100 do begin  x:= F(n);
    if x mod 3 =0 then 
      k:=k+1;
    end;
  writeln(k);
end.

