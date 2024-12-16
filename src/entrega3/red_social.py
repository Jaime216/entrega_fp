from __future__ import annotations

from dataclasses import dataclass
from datetime import date, datetime
from typing import Dict

from entrega3.grafo import Grafo
from entrega3.recorridos import bfs


@dataclass( frozen = True )
class Usuario:
    dni: str
    nombre: str
    apellidos: str
    fecha_nacimiento: date

    @staticmethod
    def of( dni: str, nombre: str, apellidos: str, fecha_nacimiento: date ) -> Usuario:
        return Usuario( dni, nombre, apellidos, fecha_nacimiento )

    def __str__( self ) -> str:
        return f"{self.dni} - {self.nombre} - {self.apellidos} - {self.fecha_nacimiento}"


@dataclass( frozen = True )
class Relacion:
    id: int
    interacciones: int
    dias_activa: int
    __n: int = 0  # Contador de relaciones. Servirá para asignar identificadores únicos a las relaciones.

    @staticmethod
    def of( interacciones: int, dias_activa: int ) -> Relacion:
        Relacion.__n += 1
        return Relacion( Relacion.__n, interacciones, dias_activa )

    def __str__( self ) -> str:
        return f"({self.id} - días activa: {self.dias_activa} - num interacciones {self.interacciones})"


class Red_social( Grafo[Usuario, Relacion] ):
    """
    Representa una red social basada en el grafo genérico.
    """

    def __init__( self, es_dirigido: bool = False ) -> None:
        super().__init__( es_dirigido )
        '''
        usuarios_dni: Diccionario que asocia un DNI de usuario con un objeto Usuario.
        Va a ser útil en la lectura del fichero de relaciones para poder acceder a los usuarios
        '''
        self.usuarios_dni: Dict[str, Usuario] = {}

    @staticmethod
    def of( es_dirigido: bool = False ) -> Red_social:
        """
        Método de factoría para crear una nueva Red Social.

        :param es_dirigido: Indica si la red social es dirigida (True) o no dirigida (False).
        :return: Nueva red social.
        """
        return Red_social( es_dirigido )

    @staticmethod
    def parse( f1: str, f2: str, es_dirigido: bool = False ) -> Red_social:
        """
        Método de factoría para crear una Red Social desde archivos de usuarios y relaciones.

        :param f1: Archivo de usuarios.
        :param f2: Archivo de relaciones.
        :param es_dirigido: Indica si la red social es dirigida (True) o no dirigida (False).
        :return: Nueva red social.
        """
        red_social = Red_social( es_dirigido )

        # Leer usuarios del archivo f1 (archivo de usuarios)
        with open( f1, 'r' ) as file_usuarios:
            for line in file_usuarios:
                # Asumimos que cada línea tiene el formato: dni, nombre, apellidos, fecha_nacimiento
                dni, nombre, apellidos, fecha_nacimiento = line.strip().split( ',' )
                fecha_nacimiento = date.fromisoformat( fecha_nacimiento )  # Convertir la fecha a un objeto date
                usuario = Usuario.of( dni, nombre, apellidos, fecha_nacimiento )
                red_social.usuarios_dni[dni] = usuario
                red_social.add_vertex( usuario )

        # Leer relaciones del archivo f2 (archivo de relaciones)
        with open( f2, 'r' ) as file_relaciones:
            for line in file_relaciones:
                # Asumimos que cada línea tiene el formato: dni1, dni2, interacciones, dias_activa
                dni1, dni2, interacciones, dias_activa = line.strip().split( ',' )
                interacciones = int( interacciones )
                dias_activa = int( dias_activa )

                # Recuperar los usuarios correspondientes a los DNIs
                usuario1 = red_social.usuarios_dni[dni1]
                usuario2 = red_social.usuarios_dni[dni2]

                # Crear la relación
                relacion = Relacion.of( interacciones, dias_activa )

                # Añadir la relación (arista) entre los usuarios
                red_social.add_edge( usuario1, usuario2, relacion )

        return red_social

