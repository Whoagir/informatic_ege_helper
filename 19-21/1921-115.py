
def win( s, M ):
    if s % 10 == 0: return M % 2 == 0
    if M == 0: return 0
    h = [ win( x, M-1 ) for x in [s+1, s+3, s+11] ]
    return any( h ) if M % 2 != 0 else \
           all( h )

arrS = [ s for s in range(11, 100) if s % 10 != 0  ]

print('19)', [ s for s in arrS if win(s, 2) ] )
print('20)', len( [ s for s in arrS if win(s, 3) and not win(s, 1) ]) )
print('21)', sum( [ s for s in arrS if win(s, 4) and not win(s, 2) ] ))

