from entrega2.tipos.Pila import Pila


def test_pila():
    # Crear una pila vacía
    pila = Pila.of()  # Crea una pila vacía

    # Añadir los números 23, 47, 1, 2, -3, 4, 5 a la pila
    numeros_a_añadir = [23, 47, 1, 2, -3, 4, 5]
    for numero in numeros_a_añadir:
        pila.add( numero )

    # Mostrar el resultado de la pila después de añadir los elementos
    print( "################################################" )
    print( "Creación de una pila vacía a la que luego se le añaden con un solo método los números: 23, 47, 1, 2, -3, 4, 5" )
    print( f"Resultado de la pila: Pila([{', '.join(map(str, pila.elements))}])\n " )

    # Eliminar un elemento de la pila, debe ser el último (operación LIFO)
    eliminado = pila.remove()
    print( "################################################" )
    print( f"Elemento eliminado de la pila: {eliminado}" )

    # Elementos eliminados utilizando remove_all
    eliminados = pila.remove_all()
    print( "################################################" )
    print( f"Elementos eliminados utilizando remove_all: {eliminados}" )


# Llamada a la función para probarla
if __name__ == '__main__':
    test_pila()
