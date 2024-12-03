// Автор: Зубов Н.С.
program n_1;
var min,k,i,del,j:integer;
begin
  min:=9999999;
  k:=0;
  del:=0;
  for i:=35612 to 57354 do begin
    for j:=1 to i do begin
      if i mod j = 0 then
        del:=del+1;
        end;
        if del>25 then begin
      if min>i then min:=i;
      k:=k+1;
      end;
   del:=0;
  end;
  writeln(k,' ',min);
end.