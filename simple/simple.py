import random


def genera_lista():
    """Función que retorno una lista de diccionarios de edades 

    Returns:
        list_edades: lista de diccionarios de longitud = 10

    >>> len(genera_lista()) == 10
    True

    >>> list_example = genera_lista()
    >>> type(list_example[0])
    <class 'dict'>
    """
    
  
    list_edades = []

    for i in range(10):

        edad_aleatoria = random.randint(0, 100)
        
        list_edades.append(dict({'id': i, 'edad':edad_aleatoria}))

    return list_edades


def ordenar_lista(list_edades):
    """Función que ordena una lista de diccionarios segun su edad.
    

    Args:
        list_edades (list):lista a ordenar

    Returns:
        list_ordenada: lista ordenada según su edad 

    >>> list_example = [{'id': 0, 'edad': 37}, {'id': 1, 'edad': 18}, {'id': 2, 'edad': 77}, {'id': 3, 'edad': 50}, {'id': 4, 'edad': 83}, {'id': 5, 'edad': 55}, {'id': 6, 'edad': 8}, {'id': 7, 'edad': 75}, {'id': 8, 'edad': 89}, {'id': 9, 'edad': 73}]
    >>> list_ordenada = ordenar_lista(list_example)
    >>> list_ordenada[0]["id"] == 6
    True
    >>> list_ordenada[9]["id"] == 8
    True
    """

    list_ordenada = sorted(list_edades, key=lambda d: d['edad'])

    return list_ordenada  


list_edades_desordenada = genera_lista()

list_edades_ordenada = ordenar_lista(list_edades_desordenada)

print(f'--> Lista ordenada por edad: \n{list_edades_ordenada}\n')
print(f'La persona más joven tiene ID:{list_edades_ordenada[0].get("id")} \nLa persona más vieja tiene ID:{list_edades_ordenada[9].get("id")}')
print("_________________________________________________________________________\n\n")
