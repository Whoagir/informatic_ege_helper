// Автор: Зубов Н.С.
program vosemtri;
var s,p,n,k,max:integer;
begin
  k:=0;
  max:=0;
for n:=1111 to 9999 do begin
  s:=(n mod 10)+(n div 1000)+((n div 100) mod 10) + ((n mod 100) div 10);
  p:=(n mod 10)*(n div 1000)*((n div 100) mod 10) * ((n mod 100) div 10);
  if p<>0 then begin
  if (n mod s=0) and (n mod p=0) then begin
    k:=k+1;
    if n>max then max:=n;
    end;
    end;
 end;
  writeln(k,' ',max);
end.