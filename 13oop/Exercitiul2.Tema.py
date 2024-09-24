"""
Problema 2.
• Creati o clasa ce va reprezenta un catalog de prajituri.
La crearea unui obiect al acestei clase, se vor solicita trei argumente, reprezentand nume (sir
de caractere), preț (integer) si gramaj (integer). Fiecare obiect creat va fi adaugat intr-o lista
mentinuta de o variabila a clasei.
Clasa trebuie sa detina o metoda care sa poate afisa toate prăjiturile sortand în funcție de
nume, gramaj sau pret.
• Creati a doua clasa care mosteneste prima clasa si care se va numi Tort.
Aceasta clasa va avea un atribut denumit etajat, care default va fi False și un alt atribut care
se numește glazura (sir de caractere) si care are default, valoarea „ciocolata”. Aceste atribute
trebuiesc implementate printr-o metoda de setare cu parametrii de intrare. O alta metoda
permite citirea acestora.
• Creati a treia clasa care mosteneste prima clasa care se va numi Fursec. Aceasta va
mosteni intocmai prima clasa fara a modifica/ adauga nimic.
Verificari:
Creati 3 obiecte ale clasei Tort si trei obiecte ale clasei Fursec.
Afisati prajiturie dupa gramaj.
Afisati prajiturie dupa pret.
Folositi pentru un obiect de tip tort modificarea atributelor etajat in True si glazura in “cacao”,
apoi pentru acest obiect folositi metoda de afisare a atributelor glazura si etajat.
De asemenea, folositi metoda de setare/afisare si pentru un alt obiect de tip tort.
"""


class Catalog:
    lista_prajituri = []

    def __init__(self, nume, pret, gramaj):
        self.nume = nume
        self.pret = pret
        self.gramaj = gramaj
        Catalog.lista_prajituri.append(self)

    def sortare(self, criteriu="nume"):
        if criteriu == "nume":
            prajituri_sortate = sorted(Catalog.lista_prajituri, key=lambda a: a.nume)
        elif criteriu == "pret":
            prajituri_sortate = sorted(Catalog.lista_prajituri, key=lambda a: a.pret)
        else:
            prajituri_sortate = sorted(Catalog.lista_prajituri, key=lambda a: a.gramaj)
        afisare_sortari = ""
        for i in prajituri_sortate:
            afisare_sortari += f"Nume {i.nume} Pret {i.pret} Gramaj {i.gramaj}\n"
        return afisare_sortari


class Tort(Catalog):
    def __init__(self, nume, pret, gramaj, glazura='ciocolata', etajat=False):
        super().__init__(nume, pret, gramaj)
        self.glazura = glazura
        self.etajat = etajat

    def setare_atribute(self, glazura, etajat):
        self.etajat = etajat
        self.glazura = glazura

    def afisare_atribute(self):
        return f"Tortul are glazura {self.glazura} si este {"etajat" if self.etajat is True else "fara etaj"}\n"


class Fursec(Catalog):
    pass


obiect1 = Tort("Mascarpone", 150, 2500)
obiect2 = Tort("Mango", 180, 3000)
obiect3 = Tort("Ciocolata", 130, 1800)
fursec1 = Fursec("Briose", 50, 150)
fursec2 = Fursec("Fursec cu fulgi de ciocolata", 30, 100)
fursec3 = Fursec("Macarons", 45, 80)
print(obiect3.sortare("gramaj"))
print(obiect3.sortare("pret"))
obiect3.setare_atribute("cacao", True)
print(obiect3.afisare_atribute())
