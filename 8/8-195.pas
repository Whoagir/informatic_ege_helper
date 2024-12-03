##
var (s,g) := ('СП', 'ЕИЯ');
var count := 0;
foreach var L in 2..8 do begin
  var c1 := g.Cartesian(L)
   .Where( a->g.All(b->a.CountOf(b)<=2) )  
   .Distinct.Count;
  if L > 2 then 
    c1 *= Length(s) + 1
  else
    c1 *= Length(s);
  Println( L, '->', c1 );
  count += c1;
end;   
println(count)
   