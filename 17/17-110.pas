// Автор: Зубов Н.С.
program n_1;
var w,t,i,n,d,m,p,k,s:integer;
begin
    k:=0;
    s:=0;
    for i:=255 to 4095 do begin
        n:=i;
        d:=0;
        t:=0;
          while n>0 do begin
          t:=n mod 3;
          if t=1 then begin
          d:=d+1;
          end;
          n:=n div 3;
          end;
        m:=i;
        p:=0;
        w:=0;
          while m>0 do begin
          w:=m mod 3;
          if w=0 then begin
          p:=p+1;
          end;
          m:=m div 3
          end;
        if (i mod 2 = 0) and (i mod 5 = 0)and (i mod 20 <> 0) and ((d=1) or (p=2)) then begin
            inc(k);
           s:=s+i;
        end;
    end;
    writeln(k,' ',s);
end.