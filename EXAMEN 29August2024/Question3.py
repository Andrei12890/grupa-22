"""
Scrie o functie care sa imparta o lista data in doua liste in functie de un
prag dat de la tastatura: una cu elemente mai mici decat un prag dat si alta
cu elemente mai mari sau egale cu acel prag.
Exemplu de Input si Output:
Input: list_example = [5,2,9,1,5,6] threshold = 5
Output: result = ([2,1],[5,9,5,6])
(2 puncte)
"""
list_example = [5, 2, 9, 1, 5, 6]
threshold = int(input("Introdu pragul: "))

def impartire_lista_dupa_pragul_dat_de_la_tastatura(lista, prag):
    elemente_mai_mici = []
    elemente_mai_mari_sau_egale = []

    for element in lista:
        if element < prag:
            elemente_mai_mici.append(element)
        else:
            elemente_mai_mari_sau_egale.append(element)
    return (elemente_mai_mici, elemente_mai_mari_sau_egale)
result = impartire_lista_dupa_pragul_dat_de_la_tastatura(list_example, threshold)
print("Result:", result)
