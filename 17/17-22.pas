// Автор: Зубов Н.С.
program n_1;
var i,k,min:integer;
begin
  k:=0;
  min:=7850;
  for i:=2477 to 7849 do begin
    if (i mod 2=0) and (i mod 5<>0) and (i mod 8<>0) and (i mod 9<>0) and (i mod 13<>0) then begin
      inc(k);
      if min>i then min:=i;
    end;
  end;
  writeln(k,' ',min);
end.