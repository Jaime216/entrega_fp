from entrega2.tipos.Lista_ordenada_sin_repeticion import Lista_ordenada_sin_repeticion

l = Lista_ordenada_sin_repeticion.of( lambda x: x[1] )

l.add( ( "Carlos", 20, 1.75 ) )
print( l.elements )

print( l.__repr__() )
