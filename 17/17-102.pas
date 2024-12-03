// Автор: Зубов Н.С.
var k,max,i,m,d,a:integer;
begin
    k:=0;
    max:=0;
    for i:=15 to 1000 do begin 
         if (i mod 7 = 6) and  (i mod 32 = 0)  then begin
             k:=k+1;
             if max<i then
             max:=i;
         end;
    end;
    writeln(k,' ',max);
end.