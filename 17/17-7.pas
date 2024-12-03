// Автор: Зубов Н.С.
program n_1;
var i,k,min:integer;
begin
   k:=0;
   min:=10000;
   for i:= 200 to 9120 do begin
       if (i mod 8 = 0) and (i mod 7 <> 0) and (i mod 11<> 0) and (i mod 17 <> 0) and (i mod 19 <> 0) then begin
       inc(k);
       if min>i then min:=i;
       end;
   end;
   writeln(k,' ',min);
end.