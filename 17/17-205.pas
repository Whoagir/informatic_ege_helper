// Автор: А. Богданов
##
var a := ReadAllLines('17-205.txt').Select(x->x.ToInteger)
         .Toarray;

var (k,smax) := (0,0);
for var i:=0 to a.High-1 do begin
  if (a[i]-a[i+1]).Divs(37*2) then begin
    k += 1;
    sMax := max( sMax,a[i]+a[i+1] );
  end;
end;

Print( k, sMax )

