// Автор: Зубов Н.С.
var k,max,i,m,d,a:integer;
begin
    k:=0;
    max:=-1000;
    for i:=-999 to 999 do begin 
         if (i mod 16 = 15) and  (i mod 12 <> 0) and  (i mod 13 <> 0) then begin
             k:=k+1;
             if max<i then
             max:=i;
         end;
    end;
    writeln(k*2,' ',max);
end.