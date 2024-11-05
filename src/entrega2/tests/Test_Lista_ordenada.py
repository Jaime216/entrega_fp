'''
Created on 6 nov 2024

@author: jcgon
'''
from entrega2.tipos.Lista_ordenada import Lista_ordenada
# Test_Lista_ordenada.py

# Prueba de la clase Lista_ordenada

# Crear una lista con el criterio de orden lambda x: x
lista = Lista_ordenada.of( lambda x: x )

# Añadir los elementos 3, 1, 2
lista.add( 3 )
lista.add( 1 )
lista.add( 2 )

# Mostrar el resultado de la lista después de añadir los elementos
print( "################################################" )
print( "Creación de una lista con criterio de orden lambda x: x" )
print( "Se añade en este orden: 3, 1, 2" )
print( f"Resultado de la lista: ListaOrdenada({', '.join(map(str, lista.elements))})\n" )

# El elemento eliminado al utilizar remove()
eliminado = lista.remove()
print( "################################################" )
print( f"El elemento eliminado al utilizar remove(): {eliminado}\n" )

lista.add( 1 )

# Elementos eliminados utilizando remove_all
eliminados = lista.remove_all()
print( "################################################" )
print( f"Elementos eliminados utilizando remove_all: {eliminados}\n" )

lista.add( 3 )
lista.add( 1 )
lista.add( 2 )
# Comprobando si se añaden los números en la posición correcta...
# Añadir el 0 y verificar el orden
lista.add( 0 )
print( "################################################" )
print( f"Lista después de añadirle el 0: ListaOrdenada({', '.join(map(str, lista.elements))})" )

# Añadir el 10 y verificar el orden
lista.add( 10 )
print( f"Lista después de añadirle el 10: ListaOrdenada({', '.join(map(str, lista.elements))})" )

# Añadir el 7 y verificar el orden
lista.add( 7 )
print( f"Lista después de añadirle el 7: ListaOrdenada({', '.join(map(str, lista.elements))})" )
