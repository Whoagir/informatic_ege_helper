// Автор: Зубов Н.С.
      program n_31;
      uses crt;
      var n, k, min, m, d:integer;
      begin
         k:=0;
         min:=10000;
         for n:=1000 to 9999 do begin
         m:=n;
         d:=0;
         while m>0 do begin
         m:= m div 5;
         d:=d+1;
         end;
         if (d >=6 ) and (((n mod 5=1) and (n div 5 mod 5=2)) or ((n mod 5=3) and (n div 5 mod 5=2))) then
         begin
         inc(k);
         if min>n then
         min:=n;
         end;
         end;
         writeln(k,' ',min);
         end.