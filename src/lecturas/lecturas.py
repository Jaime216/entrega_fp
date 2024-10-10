# Description: Funciones de lectura de archivos
import csv
from typing import Optional, Iterable


def funcion_6( file_name: str, delimitador:str, word: str ):
    apariciones: int = 0
    with open( file_name, encoding = 'UTF-8' ) as file:
        for line in file:
            words = line.split( delimitador )
            for w in words:
                if( w.strip().lower() == word.lower() ): apariciones += 1
    return apariciones


def funcion_7( file_name: str, word: str ):
    lines: Iterable[str] = []
    with open( file_name, encoding = 'UTF-8' ) as file:
            [lines.append( line ) for line in file if word.lower() in line.lower()]
    return lines


def funcion_8( file_name: str ) -> Iterable[str] | str:
    words: Iterable[str] = []
    res: Iterable[str] = []
    with open( file_name, encoding = 'UTF-8' ) as file:
        for line in file:
            line = line.replace( "\n", "" )
            words += line.split( " " )
    for word in words:
        count = 0
        for word2 in words:
            if( word2 == word ):
                count += 1
        if count == 1:
            res.append( word )
            count = 0
        else:
            count = 0
    if( len( res ) == 0 ): return "No hay palabras repetidas."
    else: return res


def funcion_9( file_path: str ) -> Optional[float]:
    number_of_lines: int = 0
    number_of_words: int = 0
    with open( file_path, mode = 'r', newline = '', encoding = 'utf-8' ) as archivo_csv:
        lector_csv = csv.reader( archivo_csv )
        # Iteramos sobre cada fila del archivo
        for line in lector_csv:
                number_of_lines += 1
                number_of_words += len( line )
    if( number_of_lines == 0 ): return None
    else: return number_of_words / number_of_lines
