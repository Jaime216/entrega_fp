'''
Created on 21 nov 2024

@author: damat

-------------
Pseudocódigo:
-------------

función bfs(grafo, inicio, destino):
    crear un conjunto vacío llamado visitados
    crear una cola vacía
    agregar inicio a la cola
    crear un diccionario llamado predecesores, donde inicio no tiene predecesor

    mientras la cola no esté vacía:
        tomar el elemento que está al frente de la cola y llamarlo vértice

        si vértice es igual a destino:
            salir del bucle

        si vértice no está en visitados:
            agregar vértice al conjunto visitados

            para cada vecino conectado a vértice en el grafo:
                si vecino no está en visitados:
                    agregar vecino a la cola
                    registrar a vértice como predecesor de vecino en predecesores

    devolver reconstruir_camino(predecesores, destino)

-------------------------------------------------------------
función dfs(grafo, inicio, destino):
    crear un conjunto vacío llamado visitados
    crear una pila vacía
    agregar inicio a la pila
    crear un diccionario llamado predecesores, donde inicio no tiene predecesor

    mientras la pila no esté vacía:
        tomar el elemento más reciente agregado a la pila y llamarlo vértice

        si vértice es igual a destino:
            salir del bucle

        si vértice no está en visitados:
            agregar vértice al conjunto visitados

            para cada vecino conectado a vértice en el grafo, en orden inverso:
                si vecino no está en visitados:
                    agregar vecino a la pila
                    registrar a vértice como predecesor de vecino en predecesores

    devolver reconstruir_camino(predecesores, destino)
-------------------------------------------------------------------------

función reconstruir_camino(predecesores, destino):
    crear una lista vacía llamada camino
    establecer vértice_actual como destino

    mientras vértice_actual no sea nulo:
        agregar vértice_actual al inicio de la lista camino
        cambiar vértice_actual al predecesor de dicho vértice_actual usando el diccionario predecesores

    devolver camino

'''
from typing import TypeVar, List, Set

from entrega2.tipos.Cola import Cola
from entrega2.tipos.Pila import Pila
from entrega3.grafo import Grafo

# Importa la clase Grafo desde su módulo
V = TypeVar( 'V' )  # Tipo de los vértices
E = TypeVar( 'E' )  # Tipo de las aristas


def bfs( grafo: Grafo[V, E], inicio: V, destino: V ) -> List[V]:
    """
    Realiza un recorrido en anchura (BFS) desde un vértice inicial hasta un vértice destino usando una Cola.

    :param grafo: Grafo sobre el que realizar la búsqueda.
    :param inicio: Vértice inicial.
    :param destino: Vértice de destino.
    :return: Lista de vértices en el camino más corto desde inicio a destino, o [] si no hay camino.
    """
    visitados = set()
    cola = Cola.of()
    cola.add( inicio )
    predesores = { inicio: None }

    while not cola.is_empty:
        vertice = cola.remove()

        vecinos = grafo.successors( vertice ) | grafo.predecessors( vertice )
        if vertice == destino:
            break

        if vertice not in visitados:
            visitados.add( vertice )

            for vecino in vecinos:
                if vecino not in visitados:
                    cola.add( vecino )
                    predesores[vecino] = vertice
    return reconstruir_camino( predesores, destino )


def dfs( grafo: Grafo[V, E], inicio: V, destino: V ) -> List[V]:
    """
    Realiza un recorrido en profundidad (DFS) desde un vértice inicial hasta un vértice destino usando una Pila.

    :param grafo: Grafo sobre el que realizar la búsqueda.
    :param inicio: Vértice inicial.
    :param destino: Vértice de destino.
    :return: Lista de vértices en el camino más corto desde inicio a destino, o [] si no hay camino.
    """
    visitados = set()
    pila = Pila.of()
    pila.add( inicio )
    predesores = { inicio: None }

    while not pila.is_empty:
        vertice = pila.remove()

        vecinos = grafo.successors( vertice ) | grafo.predecessors( vertice )
        if vertice == destino:
            break

        if vertice not in visitados:
            visitados.add( vertice )

            for vecino in reversed( list( vecinos ) ):
                if vecino not in visitados:
                    pila.add( vecino )
                    predesores[vecino] = vertice
    return reconstruir_camino( predesores, destino )


def reconstruir_camino( predecesores: dict, destino: V ) -> List[V]:
    """
    Reconstruye el camino desde el origen hasta el destino usando el diccionario de predecesores.

    :param predecesores: Diccionario que mapea cada vértice a su predecesor.
    :param destino: Vértice de destino.
    :return: Lista de vértices en el camino desde el origen hasta el destino.
    """
    camino = []
    nodo_actual = destino

    while nodo_actual != None:
        camino.append( nodo_actual )
        nodo_actual = predecesores[nodo_actual]

    return camino
