from entrega2.tipos.Cola import Cola


def test_de_cola():
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

    # Eliminar un elemento de la cola, debe ser el primero
    eliminado = cola.remove()
    print( "################################################" )
    print( f"Elemento eliminado de la cola: {eliminado}" )
    print( f"Resultado de la cola después de eliminar el primer elemento: Cola([{', '.join(map(str, cola.elements))}])\n " )

    # Elementos eliminados utilizando remove_all
    eliminados = cola.remove_all()
    print( "################################################" )
    print( f"Elementos eliminados utilizando remove_all: {eliminados}" )
    print( f"Resultado de la cola después de eliminar todos los elementos: Cola([{', '.join(map(str, cola.elements))}])\n " )


# Llamada a la función para probarla
if __name__ == '__main__':
    test_de_cola()
