// Автор: Зубов Н.С.
program n_1;
var i,k,min:integer;
begin
   k:=0;
   min:=9999999;
   for i:= 1305 to 7850 do begin
       if ((i mod 4 = 0)or(i mod 7=0)) and ((i mod 11 <> 0) and (i mod 19<> 0) and (i mod 17 <> 0) and (i mod 21 <> 0)) then begin
       inc(k);
       if min>i then min:=i;
       end;
   end;
   writeln(k,' ',min);
end.