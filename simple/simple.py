import random


def genera_lista():
    list_edades = []

    for i in range(10):

        edad_aleatoria = random.randint(0, 100)
        
        list_edades.append(dict({'id': i, 'edad':edad_aleatoria}))

    return list_edades


def ordenar_lista(list_edades):

    list_ordenada = sorted(list_edades, key=lambda d: d['edad'])

    return list_ordenada  


list_edades_desordenada = genera_lista()

list_edades_ordenada = ordenar_lista(list_edades_desordenada)

print(f'--> Lista ordenada por edad: \n{list_edades_ordenada}\n')
print(f'La persona más joven tiene ID:{list_edades_ordenada[0].get("id")} \nLa persona más vieja tiene ID:{list_edades_ordenada[9].get("id")}')
print("_________________________________________________________________________\n\n")
