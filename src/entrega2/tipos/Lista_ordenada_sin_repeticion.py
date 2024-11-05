'''
Created on 5 nov 2024

@author: jcgon
'''
from typing import Callable, TypeVar

from entrega2.tipos.Agregado_lineal import Agregado_lineal

E = TypeVar( 'E' )
R = TypeVar( 'R' )


class Lista_ordenada_sin_repeticion( Agregado_lineal ):
    '''
    classdocs
    '''

    def __init__( self, order: Callable[[E], R] ):
        '''
        Constructor
        '''
        super().__init__( [] )
        self.__order = order

    @classmethod
    def of( cls, order: Callable[[E], R] ) -> 'Lista_ordenada_sin_repeticion':
        return cls( order )

    def __index_order( self, e:E ) -> int:
        for i, current in enumerate( self._elements ):
            if self.__order( e ) < self.__order( current ):
                return i
        # Si self.__order( e ) >= self.__order( current ) para todos los elementos, se inserta al final
        return len( self._elements )

    def add( self, e:E ) -> None:
        if e not in self._elements:
            self._elements.insert( self.__index_order( e ), e )

    def __repr__( self ) -> str:
        return f"ListaOrdenadaSinRepeticion({', '.join(map(str, self._elements))})"
