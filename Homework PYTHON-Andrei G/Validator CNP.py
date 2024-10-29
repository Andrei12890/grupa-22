"""Se doreste realizarea unui validator de CNP. Mai jos se gasesc regulile.
Codul numeric personal sau CNP este codul unic al fiecărei persoane născute în România,
format din exact 13 cifre. De regulă el este atribuit la naștere fiecărui nou născut, din acest
motiv el poate fi regăsit pe certificatul de naștere. CNP figurează și pe buletinul de identitate
sau cartea de identitate precum și pe permisul de conducere. A fost introdus ca element
obligatoriu în actele de identitate, de stare civilă și în alte acte personale printr-un decret
prezidențial semnat de Nicolae Ceaușescu, la 2 martie 1978.
Format: S AA LL ZZ JJ NNN C
S
S reprezintă sexul și secolul în care s-a născut persoana care posedă acel CNP. Persoanelor
de sex masculin le sunt atribuite numerele impare iar persoanelor de sex feminin numerele
pare.
Prima cifră a CNP-ului este: (sex bărbătesc / sex femeiesc)
● 1 / 2 - născuți între 1 ianuarie 1900 și 31 decembrie 1999
● 3 / 4 - născuți între 1 ianuarie 1800 și 31 decembrie 1899
● 5 / 6 - născuți între 1 ianuarie 2000 și 31 decembrie 2099
● 7 / 8 - pentru persoanele străine rezidente în România.
● În plus 9 - pentru persoanele străine.
AA
AA este un număr format din 2 cifre și reprezintă ultimele 2 cifre din anul nașterii. O
persoană născută în anul 1970 va avea la AA 70. (SAA = 170)
Daca o persoana va avea prima cifra cu una din valorile 7,8 (rezidenti) sau 9, atunci se va
considera secolul 20. ex SAA =771 anul nasterii va fi 1971.
LL
LL este un număr format din 2 cifre și reprezintă luna nașterii persoanei.
ZZ
ZZ reprezintă ziua nașterii în format de 2 cifre. Pentru zilele de la 1 la 9 se adaugă 0 înaintea
datei. Spre exemplificare, o persoană născută în prima zi a lunii va avea codul 01.
JJ
JJ este un număr format din două cifre și este reprezentat de codul județului sau sectorului
în care s-a născut persoana ori în care avea domiciliul sau reședința în momentul acordării
C.N.P.
De exemplu, pentru Buzău acest număr este 10. Pentru București, codul este un număr din
intervalul 41 și 46 și reprezintă sectorul în care s-a născut acea persoană.
Codurile județelor sunt în ordinea alfabetică a acestora, cu unele excepții.
NNN
NNN este un număr format din 3 cifre din intervalul 001 - 999. Numerele din acest interval
se împart pe județe, birourilor de evidență a populației, astfel încât un anumit număr din acel
interval să fie alocat unei singure persoane într-o anumită zi.
C
C este cifră de control (un cod autodetector) aflată în relație cu toate celelate 12 cifre ale
CNP-ului. Cifra de control este calculată după cum urmează: fiecare cifră din CNP este
înmulțită cu cifra de pe aceeași poziție din numărul 279146358279; rezultatele sunt
însumate, iar rezultatul final este împărțit cu rest la 11. Dacă restul este 10, atunci cifra de
control este 1, altfel cifra de control este egală cu restul"""

# Format CNP: S AA LL ZZ JJ JJ1 NNN C
S = range(1, 10)
# Reprezintă sexul și secolul în care s-a născut persoana care posedă acel CNP.
AA = range(0, 100)
# Este un număr format din 2 cifre și reprezintă ultimele 2 cifre din anul nașterii.
LL = range(1, 13)
# Este un număr format din 2 cifre și reprezintă luna de naștere a acelei persoane.
ZZ = range(1, 32)
# Reprezintă ziua nașterii în format de 2 cifre.
JJ = range(0, 47)
# Este un număr format din două cifre și este reprezentat de codul județului.
JJ1 = range(51, 53)
# Reprezinta codul județelor Călărași și Giurgiu
NNN = range(0, 1000)
# Este un număr format din 3 cifre din intervalul 001 - 999.
C = range(1, 10)
# Este cifră de control (un cod autodetector) aflată în relație cu toate celelate 12 cifre ale
# CNP-ului.


CNP = input("Introduceți un CNP valid: ")

if len(CNP) != 13:
    print("CNP-ul trebuie să aibă 13 caractere!")
else:
    if int(CNP[0]) not in S:
        print("Caracterul de pe indexul 1 nu este corect! Încearcă din nou.")
    elif int(CNP[1:3]) not in AA:
        print("Caracterele de pe indexul 2 și 3 nu sunt corecte! Încearcă din nou.")
    elif int(CNP[3:5]) not in LL:
        print("Caracterele de pe indexul 4 și 5 nu sunt corecte! Încearcă din nou.")
    elif int(CNP[5:7]) not in ZZ:
        print("Caracterele de pe indexul 6 și 7 nu sunt corecte! Încearcă din nou.")
    elif int(CNP[7:9]) not in JJ and int(CNP[7:9]) not in JJ1 and CNP[7:9] == "00":
        print("Caracterele de pe indexul 8 și 9 nu sunt corecte! Încearcă din nou.")
    elif int(CNP[9:12]) not in NNN and int(CNP[9:12]) == "000":
        print("Caracterele de pe indexul 10, 11 și 12 nu sunt corecte! Încearcă din nou.")
    elif int(CNP[12]) not in C:
        print("Caracterul de pe indexul 13 nu este corect! Încearcă din nou.")
    else:

        if CNP[0] == "1":
            Sex = "Masculin, născut între 1 ianuarie 1900 și 31 decembrie 1999"
        elif CNP[0] == "2":
            Sex = "Feminin, născută între 1 ianuarie 1900 și 31 decembrie 1999"
        elif CNP[0] == "3":
            Sex = "Masculin, născut între 1 ianuarie 1800 și 31 decembrie 1899"
        elif CNP[0] == "4":
            Sex = "Feminin, născută între 1 ianuarie 1800 și 31 decembrie 1899"
        elif CNP[0] == "5":
            Sex = "Masculin, născut între 1 ianuarie 2000 și 31 decembrie 2099"
        elif CNP[0] == "6":
            Sex = "Feminin, născută între 1 ianuarie 2000 și 31 decembrie 2099"
        elif CNP[0] == "7":
            Sex = "Masculin, persoană străină rezidentă în România"
        elif CNP[0] == "8":
            Sex = "Feminin, persoană străină rezidentă în România"
        elif CNP[0] == "9":
            Sex = "Persoană străină"

        An_Nastere = CNP[1:3]

        if CNP[3:5] == "01":
            Luna_nastere = "Ianuarie"
        elif CNP[3:5] == "02":
            Luna_nastere = "Februarie"
        elif CNP[3:5] == "03":
            Luna_nastere = "Martie"
        elif CNP[3:5] == "04":
            Luna_nastere = "Aprilie"
        elif CNP[3:5] == "05":
            Luna_nastere = "Mai"
        elif CNP[3:5] == "06":
            Luna_nastere = "Iunie"
        elif CNP[3:5] == "07":
            Luna_nastere = "Iulie"
        elif CNP[3:5] == "08":
            Luna_nastere = "August"
        elif CNP[3:5] == "09":
            Luna_nastere = "Septembrie"
        elif CNP[3:5] == "10":
            Luna_nastere = "Octombrie"
        elif CNP[3:5] == "11":
            Luna_nastere = "Noiembrie"
        elif CNP[3:5] == "12":
            Luna_nastere = "Decembrie"
Zi_nastere = CNP[5:7]

print(f"{CNP} este un CNP VALID.\n"
      f"Persoana este de sexul {Sex},\n"
      f"Născut/Născută în anul {An_Nastere},\n"
      f"Luna {Luna_nastere}, Ziua {Zi_nastere}.")
