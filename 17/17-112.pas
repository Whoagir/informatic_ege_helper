// Автор: Зубов Н.С.
program n_1;
var w,t,i,n,d,m,p,k,s,max,min:integer;
begin
    k:=0;
    max:=0;
    min:=2224;
    for i:=1213 to 2223 do begin
        n:=i;
        d:=0;
        t:=0;
          while n>0 do 
            begin
          t:=n mod 10;
          if (t>6) and (t<8) then 
          d:=d+1;
          n:=n div 10;
          end;
        m:=i;
        p:=0;
        w:=0;
          while m>0 do 
          begin
          w:=m mod 10;
          p:=p+w;
          m:=m div 10
          end;
 if (i mod 2 = 0)  and (d=1) and  (p=14) then begin
            inc(k);
            if i>max then max:=i;
            if i<min then min:=i;
            end;
        end;
    writeln(k,' ',(max-min));
end.