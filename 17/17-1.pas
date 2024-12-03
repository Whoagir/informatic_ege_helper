// Автор: Зубов Н.С.
program n_1;
var i,k,max:integer;
begin
  k:=0;
  max:=0;
  for i:= 1012 to 9638 do begin
     if (i mod 3=0) and (i mod 11<>0) and (i mod 13<>0) and ( i mod 17<>0) and (i mod 19<>0) then begin
     inc(k);
     max:=i;
     end;
  end;
  writeln(k,' ',max);
end.