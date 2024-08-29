"""
Scrie un program care sa afiseze un dictionar ce contine:
-Un numar dat de utilizator (numar intreg pozitiv) care reprezinta
numarul de chei, cu prima cheie 1.
-Numarul maxim de chei admise: 15.
-Valorile pentru fiecare cheie reprezinta suma cumulativa a numerelor
de la 1 pana la cheia respectiva (de exemplu, cheie 4 - valoare 10,
deoarece 1 + 2 + 3 + 4 = 10).
Exemplu de Input si Output:
Input: Utilizatorul introduce numarul 5.
Output: Dictionar:{1:1,2:3,3:6,4:10,5:15}
(1 punct)
"""
numar_chei = int(input("Introdu un numar intreg pozitiv mai mic sau egal cu '15': "))
if numar_chei > 15:
    print("Numarul maxim de chei admise este 15! Incearca din nou!")
else:
    dictionarul_meu = {}
    for cheie in range(1, numar_chei + 1):
        suma_cumulativa = sum(range(1, cheie + 1))
        dictionarul_meu[cheie] = suma_cumulativa
    print("Dictionar:", dictionarul_meu)
