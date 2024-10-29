"""
Scrieti o functie, care sa separe o lista data de utilizator,
 in doua parti, astfel incat lungimea primei liste
 sa fie egala cu un numar dat.
model:
list_example = [1, 1, 2, 3, 4, 4, 5, 1]
first_list_length = 3
result = ([1, 1, 2], [3, 4, 4, 5, 1])
"""


def separare_lista(lista, lungime_lista):
    if lungime_lista > len(lista) or lungime_lista < 0:
        print("Lungimea specificată nu este validă! Încercați din nou!")
        return None

    prima_lista = lista[:lungime_lista]
    a_doua_lista = lista[lungime_lista:]
    return prima_lista, a_doua_lista


list_example = [1, 1, 2, 3, 4, 4, 5, 1]
first_list_length = 3
rezultat = separare_lista(list_example, first_list_length)
print("Lista rezultată este:", rezultat)
