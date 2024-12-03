// Автор: Зубов Н.С.
var i,k,min:integer;
begin
  k:=0;
  min:=99999999;
  for i:=1031 to 125888 do begin
    if (i mod 10<>5) and (frac(sqrt(i))=0) then begin
      k:=k+1;
      if (i mod 100=36) then begin
      if min>i then min:=i;
      end;
    end;
  end;
  writeln(k,' ',min);
end.