"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""


from collections import Counter
from operator import itemgetter
import itertools


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """

    with open("data.csv", 'r') as file:
        data = file.readlines()
    data = [line.replace('\n', '') for line in data]
    data = [line.split('\t') for line in data]

    suma = sum([int(line[1]) for line in data])

    return suma


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """

    with open("data.csv", 'r') as file:
        data = file.readlines()
    data = [line.replace('\n', '') for line in data]
    data = [line.split('\t') for line in data]

    letras = [line[0] for line in data]
    let_count = Counter(letras).most_common()
    let_count = list(sorted(let_count, key=itemgetter(0)))
    
    return let_count


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """

    with open("data.csv", 'r') as file:
        data = file.readlines()
    data = [line.replace('\n', '') for line in data]
    data = [line.split('\t') for line in data]

    data = sorted(data, key=itemgetter(0))
    agrup = {
        letra: sum([int(letra[1]) for letra in grupo])
        for letra, grupo in itertools.groupby(data, key=itemgetter(0))
    }
    agrup = [(letra, agrup[letra]) for letra in agrup]

    return agrup


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """

    with open("data.csv", 'r') as file:
        data = file.readlines()
    data = [line.replace('\n', '') for line in data]
    data = [line.split('\t') for line in data]

    fechas = [line[2].split('-')[1] for line in data]
    fech_count = Counter(fechas).most_common()
    fech_count = list(sorted(fech_count, key=itemgetter(0)))

    return fech_count


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """

    with open("data.csv", 'r') as file:
        data = file.readlines()
    data = [line.replace('\n', '') for line in data]
    data = [line.split('\t') for line in data]

    data = sorted(data, key=itemgetter(0))
    agrup = {
        letra: list(grupo)
        for letra, grupo in itertools.groupby(data, key=itemgetter(0))
    }

    agrup = [
        (
            letra,
            max([int(row[1]) for row in agrup[letra]]),
            min([int(row[1]) for row in agrup[letra]])
        )
        for letra in agrup 
    ]

    return agrup


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """

    with open("data.csv", 'r') as file:
        data = file.readlines()
    data = [line.replace('\n', '') for line in data]
    data = [line.split('\t') for line in data]

    diccs = [
        dicc.split(':')
        for line in data
        for dicc in line[4].split(',')
    ]

    diccs = sorted(diccs, key=itemgetter(0))
    agrup = {
        clave: list(grupo)
        for clave, grupo in itertools.groupby(diccs, key=itemgetter(0))
    }

    agrup = [
        (
            clave,
            min([int(row[1]) for row in agrup[clave]]),
            max([int(row[1]) for row in agrup[clave]])
        )
        for clave in agrup 
    ]

    return agrup


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """

    with open("data.csv", 'r') as file:
        data = file.readlines()
    data = [line.replace('\n', '') for line in data]
    data = [line.split('\t') for line in data]

    data = sorted(data, key=itemgetter(1))
    agrup = [
        (letra, [letra[0] for letra in grupo])
        for letra, grupo in itertools.groupby(data, key=itemgetter(1))
    ]

    return agrup


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    with open("data.csv", 'r') as file:
        data = file.readlines()
    data = [line.replace('\n', '') for line in data]
    data = [line.split('\t') for line in data]

    data = sorted(data, key=itemgetter(1))
    agrup = [
        (letra, sorted(set([letra[0] for letra in grupo])))
        for letra, grupo in itertools.groupby(data, key=itemgetter(1))
    ]

    return agrup


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """

    with open("data.csv", 'r') as file:
        data = file.readlines()
    data = [line.replace('\n', '') for line in data]
    data = [line.split('\t') for line in data]

    diccs = [
        dicc.split(':')
        for line in data
        for dicc in line[4].split(',')
    ]

    diccs = sorted(diccs, key=itemgetter(0))
    agrup = {
        clave: len(list(grupo))
        for clave, grupo in itertools.groupby(diccs, key=itemgetter(0))
    }

    return agrup


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """

    with open("data.csv", 'r') as file:
        data = file.readlines()
    data = [line.replace('\n', '') for line in data]
    data = [line.split('\t') for line in data]

    agrup = [
        (
            line[0],
            len(line[3].split(',')),
            len(line[4].split(','))
        ) 
        for line in data
    ]

    return agrup


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """

    with open("data.csv", 'r') as file:
        data = file.readlines()
    data = [line.replace('\n', '') for line in data]
    data = [line.split('\t') for line in data]

    letras = [[letra, line[1]] for line in data for letra in line[3].split(',')]

    letras = sorted(letras, key=itemgetter(0))
    agrup = {
        clave: sum([int(num[1]) for num in grupo])
        for clave, grupo in itertools.groupby(letras, key=itemgetter(0))
    }

    return agrup


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """

    with open("data.csv", 'r') as file:
        data = file.readlines()
    data = [line.replace('\n', '') for line in data]
    data = [line.split('\t') for line in data]

    diccs = [
        [
            line[0], dicc.split(':')[1]
        ]
        for line in data
        for dicc in line[4].split(',')
    ]

    diccs = sorted(diccs, key=itemgetter(0))
    agrup = {
        clave: sum([int(num[1]) for num in grupo])
        for clave, grupo in itertools.groupby(diccs, key=itemgetter(0))
    }

    return agrup
