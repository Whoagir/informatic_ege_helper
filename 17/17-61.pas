// Автор: Зубов Н.С.
var i,k,s:integer;
begin
  s:=0;
  k:=0;
  for i:=2738 to 7514 do begin
    if (i mod 7=0) and ( i mod 19<>0) then begin
      s:=i+s;
      inc(k);
    end;
  end;
  writeln(k,' ',s);
end.