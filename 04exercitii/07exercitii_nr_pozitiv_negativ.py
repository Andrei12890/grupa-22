"""
4. Creati un program in care utilizatorul sa introduca un numar. Calculati daca numarul
este pozitiv, zero sau negativ. In cazul in care este pozitiv validati daca este mai mic
decat 10 si afisati un mesaj de confirmare..Daca numarul este zero afisati “Numarul
este 0”, iar daca numarul este negativ atunci transformati numarul in numar pozitiv si
afisati numarul pozitiv.
"""
variabila = int(input("Numar: "))
if variabila > 0:
    print("Numarul este pozitiv")
    if variabila < 10:
        print("Numarul este mai mic ca 10")
elif variabila < 0:
    print("Numarul este negativ")
    variabila = variabila * -1
    print(variabila)
else:
    print("Numarul este 0")
