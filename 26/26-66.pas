### 
// Автор: А. Богданов

assign(input, '26-66.txt');
var (N, START) := ReadInteger2;
var active := START..START+24*3600*1000;

var a := (1..N).Sel(i->ReadInteger2)
        .SelM( \(x,y) -> |(x,1),(y=0 ? maxint : y,-1)| )
        .Ord.ToA;

var (maxK, maxT, k, t0) := (0,0,0,0);
foreach var (t, dk) in a do begin
   k += dk;
   if t in active then begin
     if k > maxK then (maxK, maxT) := (k,0);
     if k - dk = maxK then maxT += t-t0;
   end;
   t0 := t;
end;
print( maxK, maxT );  




