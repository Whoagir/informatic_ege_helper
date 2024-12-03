// Автор: Зубов Н.С.
program n_1;
var min,k,i:integer;
begin
  k:=0;
  min:=0;
  for i:=3790 to 7018 do begin
    if ((i mod 6=0) and (i mod 7<>0) and (i mod 19<>0)) and (i mod 10<>2) then begin
      inc(k);
     min:=i;
    end;
  end;
  writeln(k,' ',-min);
end.
