"""
Problema 1
Creati o clasa ce va reprezenta un catalog:
• La initializare trebuie sa oferim doi parametrii de intrare: nume si prenume
Metoda de initializare creaza un atribut denumit materii, de tip dictionar nepopulat, dar si
un atribut denumit absente, initializat la 0.
• Avem o metoda care afiseaza absente implementat cu __str__
• Avem o metoda care incrementeaza cu 1 nr. de absente
• Avem o metoda care sterge un nr. (exclusiv un numar - verifica) de absente dat (pentru
cazurile in care avem o scutire medicala) fara a deveni negativ
Creati a doua clasa numita Extensie1 care sa mosteneasca prima clasa. Clasa Extensie1 sa
aiba 3 metode:
- Prima metoda permite adaugarea prin doi parametrii de intrare: a unui sir de
caractere reprezentand materia si o lista reprezentand notele. Acesti parametrii de
intrare sunt utilizati pentru a adauga o intrare in dictionarul atribut materii al obiectului
curent. Cheia este materia (sirul de caractere) si lista reprezinta valorile.
- A doua metoda permite afisarea tuturor materilor unui student.
- A treia metoda permite afisarea materiilor si media aritmetica a fiecarei liste asociate
pentru fiecare materie in parte. Verificati daca in lista sunt elemente de tip numar si
ignorati alte valori.
Verificari:
• Creati 1 student numit Ion Roata
• Modificati argumentul absente sa fie incrementat de 3 ori prin metoda creata
• Stergeti doua absente prin metoda specificata
• Creati al doilea student numit George Cerc
• Modificati argumentul absente sa fie incrementat de 4 ori prin metoda creata
• Stergeti doua absente prin metoda specificata
• Afisati absentele fiecarui student
• Adaugati materia ”Python” impreuna cu o lista formata din 3 numere intre 1-10 pentru
fiecare student
• Adaugati materia ”Matematica” la al doilea student numit George Cerc si “Romana” pentru
studentul numit Ion Roata impreuna cu o lista formata din 3 numere intre 1-10 pentru fiecare
student
• Verificati ce materii are fiecare student prin metoda ce permite afisarea tuturor materilor
unui student.
• Verificati ce materii si ce note mediate au studentii.
"""
class Catalog:

    def __init__(self, nume, prenume):
        self.nume = nume
        self.prenume = prenume
        self.materii = {}
        self.absente = 0

    def __str__(self):
        return f"{self.nume} {self.prenume} are {self.absente} absente"

    def adauga_absente(self):
        self.absente += 1

    def stergere_absente(self, nr_absente):
        if (total_absente := self.absente - nr_absente) and total_absente > 0:
            self.absente = self.absente - nr_absente

class Extensie1(Catalog):

    def adauga_materie(self, materie, note):
        self.materii[materie] = note
        # self.materii.update({materie: note})

    def afisare_materii(self):
        afisare = f"{self.nume} {self.prenume} are materiile: \n"
        for key in self.materii:
            afisare += f"- {key}\n"
        return afisare

    def afisare_medii(self):
        afisare = f"{self.nume} {self.prenume} are materiile: \n"
        for materie, lista_note in self.materii.items():
            print(materie, lista_note)
            note = [nota for nota in lista_note if isinstance(nota, (int, float))]
            print(note)
            if len(note) == len(lista_note):
                suma = 0
                for i in lista_note:
                    suma += i
                media = suma / len(lista_note)
                afisare += f"- {materie} cu media {media}\n"

            else:
                afisare += f"- Nu exista note valide pentru materia {materie} \n"
        return afisare

student_1 = Extensie1("Ion", "Roata")
student_1.adauga_absente()
student_1.adauga_absente()
student_1.adauga_absente()
# print(student_1)
student_1.stergere_absente(2)
# print(student_1)
student_2 = Extensie1('George', 'Cerc')
student_2.adauga_absente()
student_2.adauga_absente()
student_2.adauga_absente()
student_2.adauga_absente()
# print(student_2)
student_2.stergere_absente(2)
# print(student_2)
student_1.adauga_materie('Python', [6, 7, 'a'])
student_2.adauga_materie('Python', [3, 7, 9])
student_2.adauga_materie('Matematica', [7, 4, 6])
student_1.adauga_materie('Romana', [4, 9, 10])
# print(student_1.afisare_materii())
# print(student_2.afisare_materii())
print(student_1.afisare_medii())
