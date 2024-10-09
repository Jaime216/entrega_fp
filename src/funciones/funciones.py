def funcion_1( n: int, k: int ):
    resultado: int = 1
    for i in range( k ):
        resultado *= ( n - i + 1 )
    return resultado


def funcion_2( r: int, a_1: int, k:int ):
    res: int = 1
    for i in range( 1, k + 1 ):
        res *= a_1 * r ** ( i - 1 )
    return res


def factorial( n:int ):
    res: int = 1
    for i in range( n ):
        res *= i + 1
    return res


def funcion_3( n:int, k:int ):
# n >= k
    numero_combinatorio = factorial( n ) // ( factorial( k ) * factorial( ( n - k ) ) )
    return numero_combinatorio


def funcion_4( n:int, k:int ):
# n >= k
    sumatorio: int = 0
    for i in range( k ):
        sumatorio += ( -1 ) ** i * funcion_3( k + 1, i + 1 ) * ( k - i ) ** n
    return ( 1 / factorial( k ) ) * sumatorio


def funcion_5( a: float, error: float ):

    def f( x ):return  2 * x ** 2

    def der( x ):return 4 * x

    xn = a
    for i in range( 1000 ):
        if( abs( f( xn ) ) <= error ):
            break
        else:
            xn = xn - f( xn ) / der( xn )
    return xn

