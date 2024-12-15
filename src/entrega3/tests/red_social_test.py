'''
Created on 15 dic 2024

@author: jcgon
'''
from datetime import date
from entrega4.red_social import Usuario, Relacion, Red_social


# Test para la clase Usuario
def test_usuario():
    # Crear un usuario
    usuario = Usuario.of( "25143909I", "Juan", "Pérez", date( 1990, 5, 25 ) )

    # Comprobar que los datos del usuario se guardaron correctamente
    assert usuario.dni == "25143909I", f"Expected '25143909I' but got {usuario.dni}"
    assert usuario.nombre == "Juan", f"Expected 'Juan' but got {usuario.nombre}"
    assert usuario.apellidos == "Pérez", f"Expected 'Pérez' but got {usuario.apellidos}"
    assert usuario.fecha_nacimiento == date( 1990, 5, 25 ), f"Expected {date(1990, 5, 25)} but got {usuario.fecha_nacimiento}"

    print( "Test de Usuario PASADO." )


# Test para la clase Relacion
def test_relacion():
    # Crear una relación
    relacion = Relacion.of( 10, 5 )

    # Comprobar que los datos de la relación se guardaron correctamente
    assert relacion.interacciones == 10, f"Expected 10 but got {relacion.interacciones}"
    assert relacion.dias_activa == 5, f"Expected 5 but got {relacion.dias_activa}"
    assert relacion.id == 1, f"Expected 1 but got {relacion.id}"  # Debe ser el primer ID asignado

    # Crear una segunda relación para comprobar el contador de IDs
    relacion2 = Relacion.of( 15, 7 )
    assert relacion2.id == 2, f"Expected 2 but got {relacion2.id}"

    print( "Test de Relacion PASADO." )


# Test para la clase Red_social
def test_red_social():
    # Crear una red social
    red_social = Red_social.of( es_dirigido = False )

    # Crear algunos usuarios
    usuario1 = Usuario.of( "25143909I", "Juan", "Pérez", date( 1990, 5, 25 ) )
    usuario2 = Usuario.of( "87345530M", "Ana", "Gómez", date( 1992, 7, 14 ) )

    # Añadir los usuarios a la red social
    red_social.add_vertex( usuario1 )
    red_social.add_vertex( usuario2 )

    # Comprobar que los usuarios se añadieron correctamente
    assert usuario1 in red_social.vertices(), f"Usuario {usuario1} no encontrado en los vértices."
    assert usuario2 in red_social.vertices(), f"Usuario {usuario2} no encontrado en los vértices."

    # Crear una relación entre los dos usuarios
    relacion = Relacion.of( 10, 5 )

    # Añadir la relación (arista) entre los usuarios
    red_social.add_edge( usuario1, usuario2, relacion )

    # Comprobar que la relación existe entre los dos usuarios
    assert ( usuario1, usuario2 ) in red_social.edges, "La relación no fue añadida correctamente."

    # Comprobar los detalles de la relación
    edge = red_social.edges[( usuario1, usuario2 )]
    assert edge == relacion, f"Expected relation {relacion} but got {edge}"

    print( "Test de Red_social PASADO." )


# Test para la función parse
def test_parse():
    # Crear archivos temporales para simular la entrada
    usuarios_content = "25143909I,Juan,Pérez,1990-05-25\n87345530M,Ana,Gómez,1992-07-14"
    relaciones_content = "25143909I,87345530M,10,5"

    # Escribir los contenidos en archivos temporales
    with open( "usuarios_test.txt", "w" ) as f:
        f.write( usuarios_content )

    with open( "relaciones_test.txt", "w" ) as f:
        f.write( relaciones_content )

    # Usar el método parse para crear una Red_social
    red_social = Red_social.parse( "usuarios_test.txt", "relaciones_test.txt", es_dirigido = False )

    # Comprobar que los usuarios y relaciones se han cargado correctamente
    assert "25143909I" in red_social.usuarios_dni, "Usuario con DNI '25143909I' no encontrado."
    assert "87345530M" in red_social.usuarios_dni, "Usuario con DNI '87345530M' no encontrado."

    usuario1 = red_social.usuarios_dni["25143909I"]
    usuario2 = red_social.usuarios_dni["87345530M"]

    # Comprobar que la relación ha sido añadida correctamente
    assert ( usuario1, usuario2 ) in red_social.edges, "Relación no encontrada entre los usuarios."

    # Limpiar archivos temporales después de la prueba
    import os
    os.remove( "usuarios_test.txt" )
    os.remove( "relaciones_test.txt" )

    print( "Test de parse PASADO." )


# Ejecutar las pruebas
test_usuario()
test_relacion()
test_red_social()
test_parse()
