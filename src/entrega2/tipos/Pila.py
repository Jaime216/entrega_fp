'''
Created on 6 nov 2024

@author: jcgon
'''
from typing import List, TypeVar
from entrega2.tipos.Agregado_lineal import Agregado_lineal

E = TypeVar( 'E' )


class Pila( Agregado_lineal ):
    '''
    classdocs
    '''

    def __init__( self, elements: List[E] ):
        '''
        Constructor
        '''
        super().__init__( elements )

    @classmethod
    def of( cls, elements: List[E] = [] ) -> 'Pila':
        return cls( elements )

    def add( self, element:E ) -> None:
        self._elements.append( element )

    def remove( self ) -> E:
        assert len( self._elements ) > 0, "La pila está vacía"
        return self._elements.pop( -1 )

    def __repr__( self ) -> str:
        return f"Pila({', '.join(map(str, self._elements))}"
