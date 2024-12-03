// Автор: Зубов Н.С.
program abc;
var n,k,max,m,d:integer;
begin
  k:=0;
  max:=0;
  for n:=2371 to 9432 do begin
    if (((n mod 8=5) and ((n div 8) mod 8=1)) or ((n mod 8=7)) and ((n div 8) mod 8=1)) and (n mod 3<>0) and (n mod 5<>0)
    then
      begin
        k:=k+1;;
        if n>max then max:=n;
      end;
  end;
  writeln(k,' ',max);
end.