"""
Se da sirul de numere n care contine [1, 2, 3, 4, 5, 6, 7].
Sa se insereze in acest sir dupa fiecare element par, dublul acestuia.
"""


def inserare_numar_dublu(lista):
    rezultat = []
    for numar in lista:
        rezultat.append(numar)
        if numar % 2 == 0:
            rezultat.append(numar * 2)
    return rezultat


n = [1, 2, 3, 4, 5, 6, 7]
print("Noua listă este aceasta: ", inserare_numar_dublu(n))
