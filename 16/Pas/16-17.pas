// Автор: Зубов Н.С.
function F( n: integer ): integer;
begin
  if n < 3 then begin
    Result := n+3;
    Exit;
  end;
  if n mod 3 = 0 then
    Result :=(n+2)*F(n-4)
  else
    Result := n + F(n-1)+2*F(n-2);
end;
begin
  writeln( F(20) )
end.
