// Автор: Зубов Н.С.
function F( n: integer ): integer;
begin
  if n < 1 then begin
    Result := n;
    Exit;
  end;
  if n mod 2 = 0 then
    Result := n+3* F(n-3)
  else
    Result := 5*n +2* F(n-5);
end;
begin
  writeln( F(30) )
end.
