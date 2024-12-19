'''
Created on 19 dic 2024

@author: jcgon
'''
from dataclasses import dataclass
from typing import Dict

from entrega3.grafo import Grafo
from entrega3.recorridos import dfs


@dataclass( frozen = True )
class Gen:
        nombre: str
        tipo: str
        num_mutaciones: int
        loc_cromosomas: str

        @staticmethod
        def of( nombre: str, tipo: str, num_mutaciones: int, loc_cromosomas: str ) -> 'Gen':
            assert num_mutaciones >= 0
            return Gen( nombre, tipo, num_mutaciones, loc_cromosomas )

        # formato de las lineas: TP53,supresor tumoral,256,17p13.1
        @staticmethod
        def parse( linea: str ) -> 'Gen':
            nombre, tipo, num_mutaciones, loc_cromosomas = linea.split( ',' )
            return Gen( nombre, tipo, int( num_mutaciones ), loc_cromosomas )


@dataclass( frozen = True )
class RelacionGenAGen:
    nombre_gen1: str
    nombre_gen2: str
    conexion: float  # [-1,1]

    @staticmethod
    def of( nombre_gen1: str, nombre_gen2: str, conexion: float ) -> 'RelacionGenAGen':
        assert -1 <= conexion <= 1
        return RelacionGenAGen( nombre_gen1, nombre_gen2, conexion )

    # formato de las cadenas genagen: TP53,EGFR,0.5
    @staticmethod
    def parse( linea: str ) -> 'RelacionGenAGen':
        nombre_gen1, nombre_gen2, conexion = linea.split( ',' )
        return RelacionGenAGen( nombre_gen1, nombre_gen2, float( conexion ) )

    @property
    def coexpresados( self ) -> bool:
        return self.conexion > 0.75

    @property
    def antiexpresados( self ) -> bool:
        return self.conexion < -0.75


class RedGenica( Grafo[Gen, RelacionGenAGen] ):

    def __init__( self, es_dirigido: bool = False ) -> None:
        super().__init__( es_dirigido )
        self.genes_por_nombre: Dict[str, Gen] = {}

    @staticmethod
    def of( es_dirigido: bool = False ) -> 'RedGenica':
        return RedGenica( es_dirigido )

    @staticmethod
    def parse( f1: str, f2: str, es_dirigido: bool = False ) -> 'RedGenica':
        red = RedGenica( es_dirigido )
        with open( f1, 'r' ) as f:
            for linea in f:
                gen = Gen.parse( linea.strip() )
                red.add_vertex( gen )
                red.genes_por_nombre[gen.nombre] = gen
        with open( f2, 'r' ) as f:
            for linea in f:
                genagen = RelacionGenAGen.parse( linea.strip() )  # Obtener los objetos Gen desde los nombres
                gen1 = red.genes_por_nombre.get( genagen.nombre_gen1 )
                gen2 = red.genes_por_nombre.get( genagen.nombre_gen2 )
                red.add_edge( gen1, gen2, genagen.conexion )
        return red


def tests():
    red = RedGenica.parse( './resources/genes.txt', './resources/red_genes.txt', es_dirigido = False )

    dfsred = dfs( red, Gen.parse( 'KRAS,oncogen,92,12p12.1' ), Gen.parse( 'PIK3CA,oncogen,112,3q26' ) )
    print( dfsred )

    subgraf = red.subgraph( dfsred )
    subgraf.draw( lambda_vertice = lambda vertice: vertice.nombre )


if __name__ == '__main__':
    gen1 = Gen.parse( 'TP53,supresor tumoral,256,17p13.1' )
    gen2 = Gen.of( 'EGFR', 'receptor', 512, '7p12' )
    print( gen1 )

    genagen = RelacionGenAGen.parse( 'TP53,EGFR,0.5' )
    print( genagen )

    tests()
