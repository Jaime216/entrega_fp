'''
Created on 6 nov 2024

@author: jcgon
'''
from entrega2.tipos.Cola import Cola
# Test_Cola.py

# Prueba de la clase Cola

# Crear una cola vacía
cola = Cola.of()  # Crea una cola vacía

# Añadir los números 23, 47, 1, 2, -3, 4, 5 a la cola
numeros_a_añadir = [23, 47, 1, 2, -3, 4, 5]
for numero in numeros_a_añadir:
    cola.add( numero )

# Mostrar el resultado de la cola después de añadir los elementos
print( "################################################" )
print( "Creación de una cola vacía a la que luego se le añaden con un solo método los números: 23, 47, 1, 2, -3, 4, 5" )
print( f"Resultado de la cola: Cola([{', '.join(map(str, cola.elements))}])\n " )

# Elementos eliminados utilizando remove_all
eliminados = cola.remove_all()
print( "################################################" )
print( f"Elementos eliminados utilizando remove_all: {eliminados}" )
