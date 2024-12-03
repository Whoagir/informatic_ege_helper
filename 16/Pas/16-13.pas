// Автор: Зубов Н.С.
function F( n: integer ): integer;
begin
  if n < 3 then begin
    Result := 2*n;
    Exit;
  end;
  if n mod 2 = 0 then
    Result :=3*n+5+ F(n-2)
  else
    Result := n +2* F(n-6);
end;
begin
  writeln( F(61) )
end.
