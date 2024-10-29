"""
Scrieti o functie care sa calculeze suma tuturor
numerelor dintr-un tuplu dat.
model:
tuple_example = (8, 2, 3, 0, 7)
result = 20
"""
def suma_tuplu(tuplu):
    return sum(tuplu)

tuple_example = (8, 2, 3, 0, 7)
rezultat = suma_tuplu(tuple_example)
print("Suma tuturor numerelor din acest tuplu este:", rezultat)
