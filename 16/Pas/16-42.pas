// Автор: Зубов Н.С.
program ss;
function G(n :integer): integer; forward;
function F(n :integer): integer;
begin
  if n = 1 then begin 
    Result := 1;
    exit;
    end;
  if n>1 then begin
    Result:= F(n - 1) + 3 * G(n - 1);
    exit;
    end;
end;
function G(n : integer):integer;
begin
  if n = 1 then begin
    Result := 1;
    exit;
    end;
  if n>1 then begin
    Result := F(n - 1) - 2 * G(n - 1);
    exit;
    end;
end;
begin
  writeln(F(18));
end.
//Складывать числа ответа