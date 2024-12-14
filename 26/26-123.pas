###
var b := ReadLines('26.txt').Skip(1) // пропустили M,N
  .Sel(s -> s.ToIs)
  .SelM(\(t,dt,x,y) -> |(t,x,+1),(t+dt,y,-1)|)
  .Ord.ToA;

b.GrBy(r->r[1])
  .Sel(g-> g.Ord.Agr((0,0), // Ord необязателен,т.к. был выше
     (\(m,k),\(t,i,z))-> (max(m,k+z),k+z))[0])
  .Sum.Pr;
b.Agr((0,0),
  (\(m,k),\(t,i,z))-> (max(m,k+z),k+z))[0].Pr;
  