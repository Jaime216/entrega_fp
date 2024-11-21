'''
Created on 21 nov 2024

@author: jcgon
'''
from abc import abstractmethod, ABC
from typing import List, TypeVar, Generic, Callable

E = TypeVar( 'E' )


class Agregado_lineal( ABC, Generic[E] ):
    '''
    classdocs
    '''

    def __init__( self, elements:List[E] ):
        '''
        Constructor
        '''
        self._elements = elements

    @property
    def elements( self ) -> List[E]:
        return self._elements

    @property
    def size( self ) -> int:
        return len( self._elements )

    @property
    def is_empty( self ) -> bool:
        return len( self._elements ) == 0

    @abstractmethod
    def add( self, element:E ) -> None:
        pass

    def add_all( self, ls:List[E] ) -> None:
        for e in ls:
            self.add( e )

    def remove( self ) -> E:
        assert len( self._elements ) > 0, "El agregado está vacío"
        return self._elements.pop( 0 )

    def remove_all( self ) -> List[E]:
        assert not self.is_empty, "El agregado está vacío"
        deleted = []
        for _ in range( self.size ):
            deleted.append( self.remove() )
        return deleted

    def contains( self, e:E ) -> bool:
        return e in self._elements

    def find( self, func: Callable[[E], bool] ) -> E | None:
        for e in self._elements:
            if func( e ):
                return e
        return None

    def filter( self, func: Callable[[E], bool] ) -> List[E]:
        res = []
        for e in self._elements:
            if func( e ):
                res.append( e )
        return res


H = TypeVar( 'H' )


class ColaConLimite( Agregado_lineal ):
    '''
    classdocs
    '''

    def __init__( self, capacidad: int, elements: List[H] = [] ):
        '''
        Constructor
        '''
        self.capacidad = capacidad
        super().__init__( elements )

    @classmethod
    def of( cls, capacidad: int ) -> 'ColaConLimite':
        return cls( capacidad )

    @property
    def is_full( self ) -> bool:
        return len( self._elements ) >= self.capacidad

    def add( self, element ):
        if len( self._elements ) >= self.capacidad:
            raise OverflowError( "La cola está llena." )
        self._elements.append( element )


def test_cola_con_limite():
    cola = ColaConLimite.of( 15 )
    print( cola.is_full )  # Debe imprimir: Falsel )
    for i in range( 15 ):
        cola.add( f"Tarea {i +1}" )
    print( cola.elements )
    print( cola.contains( "Tarea 8" ) )  # Debe imprimir: True

    print( cola.contains( "Tarea 20" ) )  # Debe imprimir: True
    print( cola.find( lambda x: "14" in x ) )
    print( cola.filter( lambda x: "2" in x ) )
    try:
        print( cola.is_full )  # Debe imprimir: True)
        cola.add( "Tarea 17" )  # Debe lanzar OverflowError
    except OverflowError as e:
        print( e )
    print( "Elemento eliminado: " + cola.remove() )  # Debe imprimir: 'Tarea 1'


if __name__ == '__main__':
    test_cola_con_limite()
