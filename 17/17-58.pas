// Автор: Зубов Н.С.
program n_1;
var k,s,i:integer;
begin
  k:=0;
  s:=0;
  for i:= 1705 to 7474 do begin
    if (i mod 11=0) and (i mod 19<>0) then begin
      inc(k);
      s:=s+i;
    end;
  end;
  writeln(k,' ',s);
end.