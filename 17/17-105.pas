// Автор: Зубов Н.С.
program n_1;
var k,max,i,m,d,a:integer;
begin
    k:=0;
    max:=0;
    for i:=31 to 2047 do begin
     m:=i;
     d:=0;
     while m>0 do 
     begin
         m:=m div 2;
         a:=m mod 2;
         d:=d+a;
     end;
         if (i mod 2 = 0) and (d=5) and (i mod 10 <> 0) then begin
             k:=k+1;
             if max<i then
             max:=i;
         end;
    end;
    writeln(k,' ',max);
end.