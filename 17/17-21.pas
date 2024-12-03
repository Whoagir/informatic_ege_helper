// Автор: Зубов Н.С.
program n_1;
var i,k,max:integer;
begin
  k:=0;
  max:=0;
  for i:=1221 to 9763 do begin
    if (i mod 7=0) and (i mod 2<>0) and (i mod 5<>0) and (i mod 11<>0) and (i mod 49<>0) then begin
      inc(k);
      max:=i;
    end;
  end;
  writeln(k,' ',max);
end.