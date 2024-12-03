// Автор: Зубов Н.С.
program n_1;
var i,k,max:integer;
begin
   k:=0;
   max:=0;
   for i:= 3201 to 12876 do begin
       if (i mod 4 = 0) and (i mod 7 <> 0) and (i mod 11<> 0) and (i mod 13 <> 0) and (i mod 19 <> 0) then begin
       inc(k);
       max:=i;
       end;
   end;
   writeln(k,' ',max);
end.