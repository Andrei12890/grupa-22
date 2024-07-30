"""
1. Sa se verifice daca textul introdus de la tastatura de catre un utilizator este un sir de
caractere de tip string sau un sir de numere. Utilizati instructiunea de tip if-elif-else.
In cazul in care valoarea este un sir de caractere, afisati pe ecran mesajul “Sirul de
caractere a fost gasit de Mihai”, unde Mihai reprezinta numele vostru
preluat automat de la tastatura.
"""
text_utilizator = input("Introduceti textul: ")
variabila_test_string = True
for i in text_utilizator:
    if i in "0123456789":
        variabila_test_string = False
    break
print(variabila_test_string)
if variabila_test_string is True:
    print("Sir de caractere")
else:
    print("Sir de caractere si cifre")
