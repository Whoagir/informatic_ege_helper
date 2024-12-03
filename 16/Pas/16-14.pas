// Автор: Зубов Н.С.
function F( n: integer ): integer;
begin
  if n < 0 then begin
    Result := -n;
    Exit;
  end;
  if n mod 2 = 0 then
    Result :=2*n+1+ F(n-3)
  else
    Result := 4*n +2* F(n-4);
end;
begin
  writeln( F(33) )
end.
