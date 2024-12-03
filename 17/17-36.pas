// Автор: Зубов Н.С.
program trishest;
var k,min,max,sr,n:integer;
begin
  min:=7858;
  max:=0;
  k:=0;
  sr:=0;
  for n:=2476 to 7857 do begin
    if (n mod 2=0) and (n mod 8<>0) and  ((n div 100) mod 10<=7) then 
    begin
      k:=k+1;
      if n<min then min:=n;
      if n>max then max:=n;
    end;
  end;
  sr:=(min+max) div 2;
  writeln(k,' ',sr);
end.