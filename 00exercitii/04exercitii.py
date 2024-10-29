"""
Creează o aplicație care permite utilizatorului să adauge articole
 (cu preț și cantitate) la o factură și apoi să calculeze totalul.
"""


def adauga_articole():
    factura = []
    while True:
        optiune_utilizator = input("Alege optiune")
        if optiune_utilizator == "1":
            pret = float(input("Introdu pretul"))
            cantitate = int(input("Introdu cantitate"))
            nume = input("Introdu numele")
            factura.append({"nume": nume, "pret": pret, "cantitate": cantitate}, )
        elif optiune_utilizator == "2":
            total = 0
            for articol in factura:
                total = total + articol["pret"] * articol["cantitate"]
            print(total)
        else:
            break
    return True


adauga_articole()
