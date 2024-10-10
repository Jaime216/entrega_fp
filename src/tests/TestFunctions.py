from funciones.funciones import funcion_1, funcion_3, funcion_2, funcion_4, funcion_5


def test_funcion_1( n:int , k:int ):
    res = funcion_1( n, k )
    print( f"""################################################
TEST DE LA FUNCIÓN 1:
El producto de {n} y {k} es: {res}
""" )


test_funcion_1( 4, 2 )


def test_funcion_2( a_1:int, r:int, k:int ):
    res = funcion_2( a_1 = a_1, r = r, k = k )
    print( f"""################################################
TEST DE LA FUNCIÓN 2:
El producto de la secuencia geométrica con a1 = {a_1}, r = {r} y k = {k} es: {res}""" )


test_funcion_2( a_1 = 3, r = 5, k = 2 )


def test_funcion_3( n:int, k:int ):
    res = funcion_3( n, k )
    print( f"""
################################################
TEST DE LA FUNCIÓN 3:
El número combinatorio de {n} y {k} es: {res}
""" )


test_funcion_3( 4, 2 )


def test_funcion_4( n: int, k:int ):
    res = funcion_4( n, k )
    print( f"""################################################
TEST DE LA FUNCIÓN 4:
El número S(n,k) siendo n = {n} y {k} = 2 es: {res}""" )


test_funcion_4( 4, 2 )


def test_funcion_5( a: float, error: float ):

    def f( x ):return  2 * x ** 2

    def der( x ):return 4 * x

    res = funcion_5( f, der, a, error )
    print( f"""
################################################
TEST DE LA FUNCIÓN 5:
Resultado de la función 5 con a = {a} y e = {error}, f(x) = 2x^2 y f'(x) = 4x: {res}""" )


test_funcion_5( 3, 0.001 )
