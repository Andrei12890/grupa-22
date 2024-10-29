"""
Scrieti un program care sa afiseze un dictionar ce contine:
- un numar dat de utilizator (numar intreg poztitiv), de chei,
cu prima cheie 1
- numarul maxim de chei admise: 20
- valorile pentru fiecare cheie in parte reprezinta patratul
cheii (ex. cheie 3 - valoare 9)
"""
numar_chei = int(input("Introduceți un număr întreg pozitiv pentru numărul "
                       "de chei maxim admise de '20':"))
if numar_chei > 20:
    print("Numărul maxim de chei admise este 20! Încearcă din nou!")
elif numar_chei < 1:
    print("Numărul trebuie să fie pozitiv și mai mare decât 0!")
    exit()

dictionarul_meu = {cheie: cheie ** 2 for cheie in range(1, numar_chei + 1)}
print(dictionarul_meu)
