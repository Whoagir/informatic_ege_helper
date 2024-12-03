// Автор: Зубов Н.С.
program abc;
var n,k,min,m,d:integer;
begin
  k:=0;
  min:=7084;
  for n:=2495 to 7083 do begin
    if (((n mod 16=10) and ((n div 16) mod 16=1)) or ((n mod 16=15)) and ((n div 16) mod 16=1)) and (n mod 5<>0) and (n mod 9<>0)
    then
      begin
        k:=k+1;;
        if n<min then min:=n;
      end;
  end;
  writeln(k,' ',min);
end.