'''
Created on 15 dic 2024

@author: jcgon
'''
from entrega3.grafo import Grafo


def test_add_vertex():
    grafo = Grafo.of( es_dirigido = True )
    print( "Test agregar vértices:" )

    # Añadir un vértice
    result = grafo.add_vertex( 1 )
    print( f"Se añadió el vértice 1: {result}" )  # Esperado: True

    # Intentar añadir el mismo vértice
    result = grafo.add_vertex( 1 )
    print( f"Se intentó añadir el vértice 1 otra vez: {result}" )  # Esperado: False

    # Añadir un vértice nuevo
    result = grafo.add_vertex( 2 )
    print( f"Se añadió el vértice 2: {result}" )  # Esperado: True


def test_add_edge():
    grafo = Grafo.of( es_dirigido = True )
    grafo.add_vertex( 1 )
    grafo.add_vertex( 2 )
    print( "Test agregar aristas:" )

    # Añadir una arista válida
    result = grafo.add_edge( 1, 2, 5 )
    print( f"Se añadió la arista (1 -> 2) con peso 5: {result}" )  # Esperado: True

    # Intentar añadir una arista entre vértices no existentes
    result = grafo.add_edge( 1, 3, 5 )
    print( f"Se intentó añadir la arista (1 -> 3): {result}" )  # Esperado: False

    # Verificar si la arista existe
    exists = grafo.edge_exists( 1, 2 )
    print( f"Existe la arista (1 -> 2): {exists}" )  # Esperado: True

    # Verificar arista no existente
    exists = grafo.edge_exists( 2, 1 )
    print( f"Existe la arista (2 -> 1): {exists}" )  # Esperado: False


def test_successors_and_predecessors():
    grafo = Grafo.of( es_dirigido = True )
    grafo.add_vertex( 1 )
    grafo.add_vertex( 2 )
    grafo.add_edge( 1, 2, 5 )

    print( "Test sucesores y predecesores:" )

    # Obtener sucesores de un vértice
    successors = grafo.successors( 1 )
    print( f"Sucesores de 1: {successors}" )  # Esperado: {2}

    # Obtener predecesores de un vértice
    predecessors = grafo.predecessors( 2 )
    print( f"Predecesores de 2: {predecessors}" )  # Esperado: {1}


def test_edge_weight():
    grafo = Grafo.of( es_dirigido = True )
    grafo.add_vertex( 1 )
    grafo.add_vertex( 2 )
    grafo.add_edge( 1, 2, 10 )

    print( "Test obtener peso de la arista:" )

    # Obtener el peso de una arista
    weight = grafo.edge_weight( 1, 2 )
    print( f"Peso de la arista (1 -> 2): {weight}" )  # Esperado: 10

    # Verificar arista que no existe
    weight = grafo.edge_weight( 2, 1 )
    print( f"Peso de la arista (2 -> 1): {weight}" )  # Esperado: None


def test_subgraph():
    grafo = Grafo.of( es_dirigido = True )
    grafo.add_vertex( 1 )
    grafo.add_vertex( 2 )
    grafo.add_vertex( 3 )
    grafo.add_edge( 1, 2, 5 )
    grafo.add_edge( 2, 3, 10 )

    print( "Test subgrafo:" )

    # Crear un subgrafo con vértices {1, 2}
    subgrafo = grafo.subgraph( {1, 2} )
    print( f"Subgrafo con vértices {1, 2}:" )
    for v in subgrafo.vertices():
        print( f"Vértice en subgrafo: {v}" )

    # Verificar que el subgrafo tenga las aristas correctas
    for origen in subgrafo.vertices():
        for destino in subgrafo.successors( origen ):
            print( f"Arista en subgrafo: {origen} -> {destino}" )


def test_inverse_graph():
    grafo = Grafo.of( es_dirigido = True )
    grafo.add_vertex( 1 )
    grafo.add_vertex( 2 )
    grafo.add_edge( 1, 2, 5 )

    print( "Test grafo inverso:" )

    # Obtener el grafo inverso
    grafo_inverso = grafo.inverse_graph()
    print( "Vértices en grafo inverso:" )
    for v in grafo_inverso.vertices():
        print( f"Vértice: {v}" )

    # Comprobar aristas en grafo inverso
    for origen in grafo_inverso.vertices():
        for destino in grafo_inverso.successors( origen ):
            print( f"Arista inversa: {origen} -> {destino}" )


def test_draw():
    grafo = Grafo.of( es_dirigido = True )
    grafo.add_vertex( 1 )
    grafo.add_vertex( 2 )
    grafo.add_edge( 1, 2, 5 )

    print( "Test dibujar grafo:" )
    grafo.draw( titulo = "Prueba de Grafo", lambda_vertice = str, lambda_arista = str )


# Ejecutamos las pruebas
test_add_vertex()
test_add_edge()
test_successors_and_predecessors()
test_edge_weight()
test_subgraph()
test_inverse_graph()
test_draw()
