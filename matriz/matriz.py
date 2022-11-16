import numpy as np
#descargar numpy: pip3 install numpy

# TEST MANUAL: descomentar alguna de las siguientes matriz y pasarla como parametro para generar "matrix"
#matriz1 = [[87, 98, 35, 15, 90], [88, 44, 44, 14, 41], [89, 82, 79, 60, 59], [90, 62, 19, 30, 78], [92, 58, 28, 56, 70]]
#matriz2 = [[85, 88, 89, 90, 91], [88, 44, 44, 14, 41], [20, 21, 22, 23, 59], [90, 62, 19, 30, 78], [92, 58, 28, 56, 70]]
#matriz3 = [[87, 88, 89, 90, 90], [88, 44, 44, 14, 41], [89, 82, 79, 60, 59], [90, 62, 19, 30, 78], [92, 58, 28, 56, 70]]
#matriz4 = [[7, 4, 8, 4, 9], [7, 1, 8, 0, 5], [0, 1, 3, 4, 5], [3, 4, 4, 1, 0], [0, 7, 9, 8, 7]]

indices_fila_tuple = None
indices_column_tuple = None
secuencia_encontrada = False

# matrix es una matriz aleatoria generada con numpy
matrix = np.random.randint(10, size=(5, 5))

#matrix = np.array(matriz3)


def buscar_secuencia(lista_matriz):
    """Función que recibe una lista y busca en ella si existe una secuencia numérica ascendente

    Args:
        lista_matriz (list): lista a la que se le va a buscar secuencias en sus filas y columnas

    Returns:
        (indice_comienza_secuencia, indice_termina_secuencia): tupla con los indices de comienzo y fin de la secuencia

    >>> lista1_example = [87, 88, 89, 90, 90]
    >>> buscar_secuencia(lista1_example)
    (0, 3)

    >>> lista2_example = [85, 88, 89, 90, 91]
    >>> buscar_secuencia(lista2_example)
    (1, 4)

    """
    contador_secuencia = 0

    #print(f'Lista recibida: {lista_matriz}')

    for indice_lista, elemento_lista in np.ndenumerate(lista_matriz[:4]):
        dif = lista_matriz[indice_lista[0]+1] - elemento_lista

        if dif == 1 and lista_matriz[indice_lista[0]+1] > elemento_lista:
            if contador_secuencia >= 1:
                contador_secuencia += 1
            else:
                contador_secuencia += 1
                indice_comienza_secuencia = indice_lista[0]
        else:
            contador_secuencia = 0

        if contador_secuencia == 3:
            indice_termina_secuencia = indice_lista[0]+1
            return (indice_comienza_secuencia, indice_termina_secuencia)
    


print(f'Matriz generada: \n{matrix}')

for i in range(5):
    fila_list = matrix[i]
    column_list = matrix[:, i]

    indices_fila_tuple = buscar_secuencia(fila_list)
    indices_column_tuple = buscar_secuencia(column_list)

    if indices_fila_tuple:
        secuencia_encontrada = True
        print(f'\n--> Se encontró secuencia en fila: {fila_list}')
        print(
            f'    Indices de matriz Inicio-fin: [{i}][{indices_fila_tuple[0]}] a [{i}][{indices_fila_tuple[1]}]')
    if indices_column_tuple:
        secuencia_encontrada = True
        print(f'\n--> Se encontró secuencia en columna: {column_list}')
        print(
            f'    Indices de matriz Inicio-fin: [{indices_column_tuple[0]}][{i}] a [{indices_column_tuple[1]}][{i}]')

if not secuencia_encontrada:
    print("\nNo se encontraron secuencias en la matriz")

print("_________________________________________________________________________\n\n")
