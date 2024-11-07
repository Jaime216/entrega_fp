from typing import TypeVar, List

E = TypeVar( "E" )
P = TypeVar( "P" )


class Cola_de_prioridad():

    def __init__( self ):
        self._elements = []
        self._priorities = []

    @property
    def size( self ) -> int:
        return len( self._elements )

    @property
    def is_empty( self ) -> bool:
        return self.size == 0

    @property
    def elements( self ):
        return self._elements

    def __index_order( self, priority: P ) -> int:
        for i, e in enumerate( self._priorities ):
            if( priority > e ):
                return i
        return len( self._elements )

    def add( self, e: E, priority: P ) -> None:
        index = self.__index_order( priority )
        self._elements.insert( index, e )
        self._priorities.insert( index, priority )

    def add_all( self, ls: List[tuple[E, P]] ):
        for e in ls:
            self.add( e[0], e[1] )

    def remove( self ) -> E:
        assert len( self._elements ) > 0, 'El agregado está vacío'
        self._priorities.pop( 0 )
        return self._elements.pop( 0 )

    def remove_all( self ) -> List[E]:
        assert not self.is_empty, 'El agregado está vacío'
        deleted = []
        while not self.is_empty:
            deleted.append( self.remove() )
        return deleted

    def decrease_priority( self, e: E, new_priority:P ) -> None:
        for i, ( element, priority ) in enumerate( zip( self._elements, self._priorities ) ):
            if( e == element and new_priority < priority ):
                self._elements.pop( i )
                self._priorities.pop( i )
                self.add( e, new_priority )
