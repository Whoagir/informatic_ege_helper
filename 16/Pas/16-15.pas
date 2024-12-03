// Автор: Зубов Н.С.
function F( n: integer ): integer;
begin
  if n < 5 then begin
    Result := 5-n;
    Exit;
  end;
  if n mod 3 = 0 then
    Result :=4*(n-5)*F(n-5)
  else
    Result := 3*n +2* F(n-1)+F(n-2);
end;
begin
  writeln( F(20) )
end.
