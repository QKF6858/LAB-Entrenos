from datetime import datetime
from collections import namedtuple
import csv


Entreno = namedtuple("Entreno", "tipo, fechahora, ubicacion, duracion, calorias, distancia, frecuencia, compartido")


def lee_entrenos(ruta):
    '''Lee un archivo csv y devuelve una lista de tuplas de tipo Entreno

    :param ruta: ruta del archivo CSV
    :type ruta: str
    :return: lista de tuplas de tipo Entreno
    :rtype: list
    '''
    entrenos = []
    
    with open(ruta, newline="", encoding="utf-8") as f:
        lector = csv.DictReader(f)

        for fila in lector:
            tipo = fila["tipo"]
            fechahora = datetime.strptime(fila["fechahora"], "%d/%m/%Y %H:%M")
            ubicacion = fila["ubicacion"]
            duracion = int(fila["duracion"])
            calorias = int(fila["calorias"])
            distancia = float(fila["distancia"])
            frecuencia = int(fila["frecuencia"])
            compartido = fila["compartido"] == "S"
            
            entreno = Entreno(tipo, fechahora, ubicacion, duracion,
                              calorias, distancia, frecuencia, compartido)
            entrenos.append(entreno)

    return entrenos


def tipos_entrenos(lista_entrenos):
    '''Función que devuelve una lista con los tipos de entreno en orden alfabético

    :param lista_entrenos: lista con todos los entrenos
    :type lista_entrenos: list
    :return: lista con los tipos de entrenos en orden alfabético y sin repetirse
    :rtype: list
    '''
    entrenos_filtrados = set(entreno.tipo for entreno in lista_entrenos)
    return sorted(entrenos_filtrados)


def entrenos_duracion_superior(lista_entrenos, d):
    '''Función que filtra los entrenos que tengan una duración mayor a d

    :param lista_entrenos: lista con todos los entrenos
    :type lista_entrenos: list
    :param d: valor a comparar
    :type d: int
    :return: lista con los entrenos superiores en duración a d
    :rtype: list
    '''
    entrenos_filtrados = [entreno for entreno in lista_entrenos if entreno.duracion > d]
    return entrenos_filtrados


def suma_calorias(lista_entrenos, f_inicio, f_fin):
    '''Función que suma las calorias quemadas por los entrenos en un periodo de tiempo

    :param lista_entrenos: lista con todos los entrenos
    :type lista_entrenos: list
    :param f_inicio: fecha inicial en formato dd/mm/yyyy
    :type f_inicio: str
    :param f_fin: fecha final en formato dd/mm/yyyy
    :type f_fin: str
    :return: suma de las calorias quemadas en el periodo dado
    :rtype: int
    '''
    fecha1 = datetime.strptime(f_inicio, "%d/%m/%Y")
    fecha2 = datetime.strptime(f_fin, "%d/%m/%Y")
    suma_total = sum(entreno.calorias for entreno in lista_entrenos if fecha1 <= entreno.fechahora <= fecha2)
    return suma_total