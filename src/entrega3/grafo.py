'''
Created on 21 nov 2024

@author: damat
'''
from __future__ import annotations

from typing import TypeVar, Generic, Dict, Set, Optional, Callable
import matplotlib.pyplot as plt
import networkx as nx

# Definición de tipos genéricos
V = TypeVar( 'V' )  # Tipo para vértices
E = TypeVar( 'E' )  # Tipo para aristas


class Grafo( Generic[V, E] ):
    """
    Representaciónde un grafo utilizando un diccionario de adyacencia.
    """

    def __init__( self, es_dirigido: bool = True ):
        self.es_dirigido: bool = es_dirigido
        self.adyacencias: Dict[V, Dict[V, E]] = {}  # Diccionario de adyacencia

    @staticmethod
    def of( es_dirigido: bool = True ) -> Grafo[V, E]:
        """
        Método de factoría para crear un nuevo grafo.

        :param es_dirigido: Indica si el grafo es dirigido (True) o no dirigido (False).
        :return: Nuevo grafo.
        """
        return Grafo( es_dirigido )

    def add_vertex( self, vertice: V ) -> None:
        """
        Añade un vértice al grafo si no existe.

        :param vertice: Vértice a añadir.
        """
        if vertice not in self.adyacencias:
            self.adyacencias[vertice] = {}
            return True
        else:
            return False

    def add_edge( self, origen: V, destino: V, arista: E ) -> None:
        """
        Añade una arista al grafo entre dos vértices.
        Si el grafo es no dirigido, añade la arista en ambos sentidos.

        :param origen: Vértice de origen.
        :param destino: Vértice de destino.
        :param arista: Arista a añadir.
        """
        if origen not in self.adyacencias or destino not in self.adyacencias:
            return False
        else:
            self.adyacencias[origen][destino] = arista
            if not self.es_dirigido:
                self.adyacencias[destino][origen] = arista
            return True

    def successors( self, vertice: V ) -> Set[V]:
        """
        Devuelve los sucesores de un vértice.

        :param vertice: Vértice del que se buscan los sucesores.
        :return: Conjunto de sucesores.
        """
        if vertice in self.adyacencias:
            return set( self.adyacencias[vertice].keys() )
        else:
            return Set()

    def predecessors( self, vertice: V ) -> Set[V]:
        """
        Devuelve los predecesores de un vértice.

        :param vertice: Vértice del que se buscan los predecesores.
        :return: Conjunto de predecesores.
        """
        if vertice not in self.adyacencias:
            return False
        else:
            predecesores = {v for v in self.adyacencias if vertice in self.adyacencias[v]}
            return predecesores

    def neighbors( self, vertice: V ) -> Set[V]:
        """
        Devuelve los vecinos de un vértice (sucesores y predecesores).

        :param vertice: Vértice del que se buscan los vecinos.
        :return: Conjunto de vecinos.
        """
        return self.successors( vertice ) | self.predecessors( vertice )

    def edge_weight( self, origen: V, destino: V ) -> Optional[E]:
        """
        Devuelve el peso de la arista entre dos vértices.

        :param origen: Vértice de origen.
        :param destino: Vértice de destino.
        :return: Peso de la arista, o None si no existe.
        """
        if origen in self.adyacencias and destino in self.adyacencias[origen]:
            return self.adyacencias[origen][destino]
        else:
            return False

    def vertices( self ) -> Set[V]:
        """
        Devuelve el conjunto de vértices del grafo.

        :return: Conjunto de vértices.
        """
        return set( self.adyacencias.keys() )

    def edge_exists( self, origen: V, destino: V ) -> bool:
        """
        Verifica si existe una arista entre dos vértices.

        :param origen: Vértice de origen.
        :param destino: Vértice de destino.
        :return: True si existe la arista, False en caso contrario.
        """
        if origen in self.adyacencias:
        # Verificar si el vértice de destino existe como sucesor del vértice de origen
            return destino in self.adyacencias[origen]
        return False

    def inverse_graph( self ) -> Grafo[V, E]:
        """
        Devuelve el grafo inverso (solo válido para grafos dirigidos).

        :return: Grafo inverso.
        :raise ValueError: Si el grafo no es dirigido.
        """
        if self.es_dirigido:
            grafo_inverso = Grafo.of( self.es_dirigido )
            for vertice in self.vertices():
                grafo_inverso.add_vertex( vertice )
            for origen in self.vertices():
                for destino, arista in self.adyacencias[origen].items():
                    grafo_inverso.add_edge( destino, origen, arista )
            return grafo_inverso

    def draw( self, titulo: str = "Grafo",
            lambda_vertice: Callable[[V], str] = str,
            lambda_arista: Callable[[E], str] = str ) -> None:
        """
        Dibuja el grafo utilizando NetworkX y Matplotlib. las funciones lambda permiten personalizar la representación
        de los vértices y aristas.

        :param titulo: Título del gráfico
        :param lambda_vertice: Función lambda para representar los vértices
        :param lambda_arista: Función lambda para representar las aristas
        """
        # Crear un grafo de NetworkX
        G = nx.DiGraph() if self.es_dirigido else nx.Graph()

        # Añadir nodos y aristas
        for vertice in self.vertices():
            G.add_node( vertice, label = lambda_vertice( vertice ) )  # Usamos lambda_vertice para personalizar el nodo
        for origen in self.vertices():
            for destino, arista in self.adyacencias[origen].items():
                G.add_edge( origen, destino, label = lambda_arista( arista ) )  # Usamos lambda_arista para personalizar la arista

        # Dibujar el grafo
        pos = nx.spring_layout( G )  # Distribución de los nodos
        plt.figure( figsize = ( 8, 6 ) )
        nx.draw( G, pos, with_labels = True, node_color = "lightblue", font_weight = "bold", node_size = 500,
                labels = nx.get_node_attributes( G, 'label' ) )  # Usamos las etiquetas personalizadas de los vértices

        # Dibujar las etiquetas de las aristas (con la representación personalizada)
        edge_labels = nx.get_edge_attributes( G, "label" )
        nx.draw_networkx_edge_labels( G, pos, edge_labels = edge_labels )

        plt.title( titulo )
        plt.show()

    def __str__( self ) -> str:
        """
        Representación textual del grafo.

        Formato libre. Por ejemplo:
            vertice1 -> vertice2 (peso), vertice3 (peso)
            vertice2 -> vertice1 (peso)
            ...
        """

    def subgraph( self, vertices: Set[V] ) -> Grafo[V, E]:
        """
        Crea un subgraph basado en un conjunto de vértices.

        :param vertices: Conjunto de vértices del subgraph.
        :return: Nuevo grafo con los vértices y aristas correspondientes.
        """
        subgrafo = Grafo.of( self.es_dirigido )
        for vertice in vertices:
            subgrafo.add_vertex( vertice )
        for origen in vertices:
            for destino, arista in self.adyacencias[origen].items():
                if destino in vertices:
                    subgrafo.add_edge( origen, destino, arista )
        return subgrafo

