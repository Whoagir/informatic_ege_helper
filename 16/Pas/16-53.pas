// Автор: Зубов Н.С.
function F( n: integer ): integer;
begin
  if n >15  then begin
    Result := n*n-5;
    exit;
    end;
  if n<=15 then begin
    Result :=n * F(n+2)+n+F(n+3);
    exit;
    end;
end;
begin
  writeln( F(1) )
end.
//Сумма цифр числа есть ответ
