'''
Created on 6 nov 2024

@author: jcgon
'''
from typing import List, TypeVar
from entrega2.tipos.Agregado_lineal import Agregado_lineal

E = TypeVar( 'E' )


class Cola( Agregado_lineal ):
    '''
    classdocs
    '''

    def __init__( self, elements: List[E] ):
        '''
        Constructor
        '''
        super().__init__( elements )

    @classmethod
    def of( cls, elements: List[E] = [] ) -> 'Cola':
        return cls( elements )

    def add( self, element:E ) -> None:
        self._elements.append( element )

    def __repr__( self ) -> str:
        return f"Cola({', '.join(map(str, self._elements))}"
