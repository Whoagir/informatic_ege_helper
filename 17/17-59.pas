// Автор: Зубов Н.С.
program n_1;
var k,s,i:integer;
begin
  k:=0;
  s:=0;
  for i:= 1213 to 8310 do begin
    if (i mod 3=0) and (i mod 23<>0) then begin
      inc(k);
      s:=s+i;
    end;
  end;
  writeln(k,' ',s);
end.