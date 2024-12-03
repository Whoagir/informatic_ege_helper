// Автор: Зубов Н.С.
function F( n: integer ): integer;
begin
  if n < 5 then begin
    Result := 1+2*n;
    Exit;
  end;
  if n mod 3 = 0 then
    Result :=2*(n+1)*F(n-2)
  else
    Result := 2*n +1+ F(n-1)+2*F(n-2);
end;
begin
  writeln( F(15) )
end.
