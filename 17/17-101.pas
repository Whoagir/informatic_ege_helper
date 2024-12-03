// Автор: Зубов Н.С.
var k,max,i,m,d,a:integer;
begin
    k:=0;
    max:=0;
    for i:=99 to 998 do begin 
         if (i mod 10 = 9) and  (i mod 8 = 1) and  (i mod 18 <> 0) then begin
             k:=k+1;
             if max<i then
             max:=i;
         end;
    end;
    writeln(k,' ',max);
end.