from lecturas.lecturas import funcion_6, funcion_7, funcion_8, longitud_promedio_lineas


def test_funcion_6( file_name: str, delimitador: str, word: str ):
    res = funcion_6( file_name, delimitador, word )
    print( f"""################################################
TEST DE LA FUNCIÓN 6:
El número de veces que aparece la palabra {word} en el fichero {file_name.strip("/")[3]} es: {res}
""" )


test_funcion_6( "../../resources/lin_quijote.txt", " ", "quijote" )


def test_funcion_7( file_name: str, word: str ):
    list = funcion_7( file_name, word )
    print( f"""################################################
TEST DE LA FUNCIÓN 7:
Las líneas en las que aparece la palabra {word} son: {list}
    """ )


test_funcion_7( "../../resources/lin_quijote.txt", "quijote" )


def test_funcion_8( file_name: str ):
    res = funcion_8( file_name )
    print( f"""################################################
TEST DE LA FUNCIÓN 8:
Las palabras únicas en el fichero {file_name} son: {res}""" )


test_funcion_8( "../../resources/archivo_palabras.txt" )


def test_funcion_9( file_name: str ):
    res = longitud_promedio_lineas( file_name )
    print( f"""################################################
TEST DE LA FUNCIÓN 9:
La longitud promedio de las líneas del fichero {file_name} es: {res}""" )


test_funcion_9( "../../resources/vacio.csv" )
test_funcion_9( "../../resources/palabras_random.csv" )
