'''
Created on 24 oct 2024

@author: jcgon
'''

from typing import List, Tuple


def P2( n:int, k:int, i:int = 1 ):
    assert n >= k and n > 0 and k > 0 and i > 0 and i < k + 1, "Los números deben ser positivos y i < k + 1"
    resultado = 1
    for e in range( i, k - 1 ):
        resultado *= ( n - e + 1 )
    return resultado


def factorial( n:int ):
    resultado = 1
    for e in range( 1, n + 1 ):
        resultado *= e
    return resultado


def C2( n:int, k:int ):
    assert n >= k and n > 0 and k >= 0, "Los números deben ser positivos y n >= k"
    return factorial( n ) // ( factorial( k + 1 ) * factorial( n - ( k + 1 ) ) )


def S2( n:int, k:int ):
    assert n >= k and n > 0 and k > 0, "Los números deben ser positivos y n >= k."
    primera_parte = factorial( k ) / ( n * factorial( k + 2 ) )
    segunda_parte = 0

    for i in range( k + 1 ):
        segunda_parte += ( ( -1 ) ** i ) * C2( k, i ) * ( ( k - i ) ** ( n + 1 ) )

    return primera_parte * segunda_parte


def palabrasMasComunes( fichero: str, n: int = 5 ) -> List[Tuple[str, int]]:
    # Validar que n es mayor que 1
    if n <= 1:
        raise ValueError( "n debe ser mayor que 1" )

    # Leer el contenido del archivo
    with open( fichero, 'r', encoding = 'utf-8' ) as file:
        contenido = file.read().lower()  # Convertir a minúsculas

    # Reemplazar caracteres no alfabéticos con espacios y dividir en palabras
    palabras = ''.join( char if char.isalnum() else ' ' for char in contenido ).split()

    # Contar las ocurrencias de cada palabra usando un diccionario
    contador = {}
    for palabra in palabras:
        if palabra in contador:
            contador[palabra] += 1
        else:
            contador[palabra] = 1

    contador_ordenado = sorted( contador.items(), key = lambda item: item[1], reverse = True )

    mas_comunes = contador_ordenado[:n]

    return mas_comunes


def pruebas_P2():
    print( "Pruebas para P2:" )

    # Casos válidos
    try:
        print( P2( 5, 3 ) )  # Caso válido: n > k
        print( P2( 6, 6 ) )  # Caso válido: n = k
    except Exception as e:
        print( f"Error: {e}" )

    # Casos inválidos
    try:
        print( P2( 2, 3 ) )  # Caso inválido: n < k
    except Exception as e:
        print( f"Error: {e}" )
    try:
        print( P2( 5, 4, -1 ) )  # Caso inválido: i negativo
    except Exception as e:
        print( f"Error: {e}" )
    try:
        print( P2( 5, -4 ) )  # Caso inválido: k negativo
    except Exception as e:
        print( f"Error: {e}" )
    try:
        print( P2( -5, 4 ) )  # Caso inválido: n negativo
    except Exception as e:
        print( f"Error: {e}" )

    try:
        print( P2( 5, 4, 6 ) )  # Caso inválido: i > k + 1
    except Exception as e:
        print( f"Error: {e}" )

    try:
        print( P2( 5, 4, 5 ) )  # Caso inválido: i = k + 1
    except Exception as e:
        print( f"Error: {e}" )


pruebas_P2()


def pruebas_C2():
    print( "\nPruebas para C2:" )
    try:
        print( C2( 5, 5 ) )  # Caso válido: n = k
        print( C2( 7, 5 ) )  # Caso válido: n > k
    except Exception as e:
        print( f"Error: {e}" )

    try:
        print( C2( 2, 3 ) )  # Caso inválido: n < k
    except Exception as e:
        print( f"Error: {e}" )

    try:
        print( C2( -5, 4 ) )  # Caso inválido: n negativo
    except Exception as e:
        print( f"Error: {e}" )

    try:
        print( C2( 5, -4 ) )  # Caso inválido: k negativo
    except Exception as e:
        print( f"Error: {e}" )


pruebas_C2()


def pruebas_S2():
    print( "\nPruebas para S2:" )
    try:
        print( S2( 8, 4 ) )  # Caso válido: n > k
        print( S2( 5, 5 ) )  # Caso válido: n = k
    except Exception as e:
        print( f"Error: {e}" )

    try:
        print( S2( 2, 3 ) )  # Caso inválido: n < k
    except Exception as e:
        print( f"Error: {e}" )

    try:
        print( S2( -5, 4 ) )  # Caso inválido: n negativo
    except Exception as e:
        print( f"Error: {e}" )

    try:
        print( S2( 5, -4 ) )  # Caso inválido: k negativo
    except Exception as e:
        print( f"Error: {e}" )


pruebas_S2()


def pruebas_palabrasMasComunes():
    print( "\nPruebas para palabrasMasComunes:" )
    try:
        print( palabrasMasComunes( '../../resources/archivo_palabras.txt', 5 ) )
    except Exception as e:
        print( f"Error: {e}" )
    try:
        print( palabrasMasComunes( '../../resources/archivo_palabras.txt', 0 ) )  # Caso no valido: n < 1
    except Exception as e:
        print( f"Error: {e}" )


pruebas_palabrasMasComunes()
