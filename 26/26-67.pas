## 
// Автор: А. Богданов
// Модификация: К. Поляков

assign(input, '26-66.txt');
var (N, START) := ReadInteger2;
var active := START..START+24*3600*1000;

var a := 
 ((1..N).Select(i->ReadInteger2)
        .SelectMany( \(x,y) -> |(x,1),(y=0 ? maxint : y,-1)| ) +
        |(START,1), (START,-1)|)  
        .OrderBy(\(x,y)->(x,-y)).ToArray;

var (minK, minT, k, t0) := (10**10, 0, 0, 0);
foreach var (t, dk) in a do begin
   k += dk;
   if t in active then begin
     if k < minK then (minK, minT) := (k, 0);
     if k - dk = minK then minT += t - t0;
   end;
   t0 := t;
end;
print( minK, minT );  




