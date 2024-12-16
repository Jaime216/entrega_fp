'''
Created on 16 dic 2024

@author: jcgon
'''
from entrega3.recorridos import bfs
from entrega3.red_social import Red_social

if __name__ == '__main__':
    raiz = '../'  # Cambia esta variable si ejecutas este script desde otro directorio
    rrss = Red_social.parse( raiz + 'resources/usuarios.txt', raiz + 'resources/relaciones.txt', es_dirigido = False )

    if rrss:
        sep = '\n'
        print( "************** Nº Predecesores de cada vértice" )
        print( sep.join( f'{v} -- {len(rrss.predecessors(v))}'  for v in rrss.vertices() ) )

        print( "\n************** Nº Vecinos de cada vértice" )
        print( sep.join( f'{v} -- {len(rrss.neighbors(v))}'  for v in rrss.vertices() ) )
    else:
        print( "Error al crear la red social." )

    print( "El camino más corto desde 25143909I hasta 87345530M es:" )
    camino = bfs( rrss, rrss.usuarios_dni['25143909I'], rrss.usuarios_dni['87345530M'] )
    g_camino = rrss.subgraph( camino )

    g_camino.draw( "caminos", lambda_vertice = lambda v: f"{v.dni}", lambda_arista = lambda e: e.id )
