# Description: Funciones de lectura de archivos
import csv
from typing import Optional


def funcion_6( file_name: str, delimitador:str, word: str ):
    apariciones = 0
    with open( file_name, encoding = 'UTF-8' ) as file:
        for line in file:
            words = line.split( delimitador )
            for w in words:
                if( w.strip().lower() == word.lower() ): apariciones += 1
    return apariciones


def funcion_7( file_name: str, word: str ):
    lines = []
    with open( file_name, encoding = 'UTF-8' ) as file:
        for line in file:
            if word.lower() in line.lower(): lines.append( line )
    return lines


def funcion_8( file_name: str ):
    txt = ""
    words = []
    res = []
    with open( file_name, encoding = 'UTF-8' ) as file:
        for line in file:
            line.replace( "\n", "" )
            txt += line
            words += line.replace( "\n", "" ).split( " " )
    for word in words:
        count = 0
        ls = txt.split( ' ' )
        for l in ls:
            if l.lower().strip() == word.lower().strip() and ( l in res ) == False:
                count += 1
        if count == 1:
            res.append( word )
        else:
            count = 0

    return res


def longitud_promedio_lineas( file_path: str ) -> Optional[float]:
    lines = 0
    words = 0
    with open( file_path, mode = 'r', newline = '', encoding = 'utf-8' ) as archivo_csv:
        lector_csv = csv.reader( archivo_csv )
        # Iteramos sobre cada fila del archivo
        for line in lector_csv:
                lines += 1
                words += len( line )
    print( lines, words )
    if( lines == 0 ): return None
    else: return words / lines
