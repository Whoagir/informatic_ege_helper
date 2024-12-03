// Автор: Зубов Н.С.
program n_1;
var k,s,i:integer;
begin
  k:=0;
  s:=0;
  for i:=1753 to 7420 do begin
    if (i mod 11=0) and (i mod 13<>0) then begin
      inc(k);
      s:=s+i;
    end;
  end;
  writeln(k,' ',s);
end.