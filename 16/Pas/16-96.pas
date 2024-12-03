// Автор: Зубов Н.С.
var s,n:integer;
function G (n:integer):integer;forward;
function F (n:integer):integer;
begin
if n<10 then 
  F:=n
else 
  F:=n mod 10 +F(n div 10);
end;
function G(n:integer):integer;
begin
if n<10 then 
  G:=n
else 
  G:=G(F(n));
end;
begin
s := 0;
for n := 10  to 99 do
s:= G(n)+s;       
write(s);
end.