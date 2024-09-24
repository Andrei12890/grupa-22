"""
Creati o clasa care sa calculeze si sa returneze operatia matematica de mai jos pentru
4 numere: [a(b+3)/c]*d.
Clasa trebuie sa aiba 2 metode: prima metoda este metoda speciala init.
Iar cea dea doua metoda este metoda speciala str.
Va rog sa aplicati cel putin doua exemple (doua obiecte).
Metoda init trebuie sa foloseasca parametrii default a=1,b=2,c=3,d=4 si trebuie sa suprime
orice eroare.
La aparitia unei erori trebuie sa afiseze textul: <>
Folositi clasa in trei exemple:
• cu patru parametrii numerici diferiti de cei default
• cu 3 parametrii non-numerici
• cu 2 parametrii numerici
"""



class Operatie:
    def __init__(self, a=1, b=2, c=3, d=4):
        try:
            self.a = float(a)
            self.b = float(b)
            self.c = float(c)
            self.d = float(d)
            self.operatia = (self.a *(self.b +3) / self.c) *self.d
        except Exception:
            self.operatia = "<>"

    def __str__(self):
        return f"Rezultatul este {self.operatia}"


operatie1 = Operatie(5, 5, 6, 8)
operatie2 = Operatie("a", "v", "f")
operatie3 = Operatie(6, 9)

print(operatie1)
print(operatie2)
print(operatie3)
