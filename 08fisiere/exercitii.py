"""
Creează un program care convertește o sumă dintr-o monedă în alta folosind un curs de schimb fix.
"""


def schimb():
    curs_schimb = float(input("Alegeti curs valutar: "))
    suma = float(input("Alegeti suma: "))
    valoare = suma * curs_schimb
    return valoare

schimb_valutar = schimb()
print(schimb_valutar)
