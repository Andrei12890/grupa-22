"""
5. Creati un program care are ca scop un meniu. Meniul se va selecta prin introducerea
de la tastaura a unui numar intre 1 si 5 captat intr-o variabila. Prezentati prin afisare
acest sir de caractere:
“”” 1 – Afisare lista de cumparaturi
2 – Adaugare element
3 – Stergere element
4 – Sterere lista de cumparaturi
5 - Cautare in lista de cumparaturi “””
Apoi folosindu-va de o constructie if-elif-else afisati: - daca utilizatorul scrie de la
tastaura 1 afisati “Afisare lista de cumparaturi” - daca utilizatorul scrie de la tastaura 2
afisati “Adugare element” - daca utilizatorul scrie de la tastaura 3 afisati “Stergere
element” - daca utilizatorul scrie de la tastaura 4 afisati “Sterere lista de cumparaturit”
- daca utilizatorul scrie de la tastaura 5 afisati “Adaugare element” - daca utilizatorul
scrie altceva de la tastaura afisati “Alegerea nu exista. Reincercati”
"""
meniu = input("Alegeti un numar din meniu: ")
lista_de_cumparaturi = ["paine", "legume", "fructe", "carne", "oua"]
if meniu == "1":
    print(lista_de_cumparaturi)
elif meniu == "2":
    adaugare_element = input("Adaugare element: ")
    lista_de_cumparaturi.append(adaugare_element)
    print(lista_de_cumparaturi)
elif meniu == "3":
    print(lista_de_cumparaturi)
    stergere_element = input("Stergere element: ")
    if stergere_element in lista_de_cumparaturi:
        lista_de_cumparaturi.remove(stergere_element)
        print(lista_de_cumparaturi)
elif meniu == "4":
    print("Sterge lista de cumparaturi")
    lista_de_cumparaturi.clear()
    print(lista_de_cumparaturi)
elif meniu == "5":
    print("Cautare in lista de cumparaturi")
    cautare_element = input("Ce element cautati: ")
    if cautare_element in lista_de_cumparaturi:
        print("Elementul exista")
    else:
        print("Alegerea nu exista. Reincercati")
