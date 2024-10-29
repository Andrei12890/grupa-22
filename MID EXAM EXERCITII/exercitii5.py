"""
Sa se scrie un program care sa calculeze impartirea
dintre trei numere. Daca valorile sunt egale, returnati
de trei ori rezultatul. Impartirea la 0 va duce la rezultatul 0.
"""
def impartirea_trei_numere(a, b, c):
    if b == 0 or c == 0:
        return 0

    rezultat = a / b / c
    if a == b == c:
        return rezultat, rezultat, rezultat
    return rezultat

a = int(input("Introdu primul număr: "))
b = int(input("Introdu al doilea număr: "))
c = int(input("Introdu al treilea număr: "))
print("Rezultatul împărțirii este: ", impartirea_trei_numere(a, b, c))
