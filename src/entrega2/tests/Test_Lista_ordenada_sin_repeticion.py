'''
Created on 6 nov 2024

@author: jcgon
'''
from entrega2.tipos.Lista_ordenada_sin_repeticion import Lista_ordenada_sin_repeticion
# Test_Lista_ordenada_sin_repeticion.py

# Prueba de la clase Lista_ordenada_sin_repeticion

# Crear una lista con el criterio de orden lambda x: -x (ordena en orden descendente)
lista = Lista_ordenada_sin_repeticion.of( lambda x:-x )

# Añadir los elementos 23, 47, 47, 1, 2, -3, 4, 5
# El elemento 47 se añade solo una vez debido a que la lista no permite duplicados

# Mostrar el resultado de la lista después de añadir los elementos
print( "################################################" )
print( "Creación de una lista con criterio de orden lambda x: -x" )
print( "Se añade en este orden: 23, 47, 47, 1, 2, -3, 4, 5" )
lista.add( 23 )
lista.add( 47 )
lista.add( 47 )
lista.add( 1 )
lista.add( 2 )
lista.add( -3 )
lista.add( 4 )
lista.add( 5 )
print( f"Resultado de la lista ordenada sin repetición: ListaOrdenadaSinRepeticion({', '.join(map(str, lista.elements))})\n" )

# El elemento eliminado al utilizar remove()
eliminado = lista.remove()
print( "################################################" )
print( f"El elemento eliminado al utilizar remove(): {eliminado}\n" )

lista.add( 47 )
# Elementos eliminados utilizando remove_all
eliminados = lista.remove_all()
print( "################################################" )
print( f"Elementos eliminados utilizando remove_all: {eliminados}\n" )

lista.add( 23 )
lista.add( 47 )
lista.add( 47 )
lista.add( 1 )
lista.add( 2 )
lista.add( -3 )
lista.add( 4 )
lista.add( 5 )
# Añadir el 0 y verificar el orden
lista.add( 0 )
print( "################################################" )
print( "Comprobando si se añaden los números en la posición correcta..." )
print( f"Lista después de añadirle el 0: ListaOrdenadaSinRepeticion({', '.join(map(str, lista.elements))})" )
lista.add( 0 )
print( f"Lista después de añadirle el 0: ListaOrdenadaSinRepeticion({', '.join(map(str, lista.elements))})" )

# Añadir el 7 y verificar el orden
lista.add( 7 )
print( f"Lista después de añadirle el 7: ListaOrdenadaSinRepeticion({', '.join(map(str, lista.elements))})\n" )
