// Автор: Зубов Н.С.
function F( n: integer ): integer;
begin
  if n = 1 then begin
    Result := 1;
    Exit;
  end;
  if n mod 2 = 0 then
    Result := 2* F(n-1)
  else
    Result := 5*n + F(n-2);
end;
begin
  writeln( F(64) )
end.
