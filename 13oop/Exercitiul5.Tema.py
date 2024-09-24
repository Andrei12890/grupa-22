"""
Creati un program ce are o clasa numita util. Clasa are o variabila a clasei de tip lista
populata automat in constructor(__init__) cu obiectul.
Creati a doua clasa numita izatori care primeste in constructor doua argumente numite
user si passw, formand cu ajutorul acestora doua atribute cu acelasi nume.
Creati a treia clasa numita utilizatori care sa mosteneasca clasele util și izatori fără a
pierde din functionalitatea claselor mostenite.
De asemenea, aceasta clasa are o metoda privata numita parole care sa returneze un
set cu toate parolele și o metoda privata numita useri care sa returneze un set cu toți
userii. Se va folosi variabila clasei de tip lista care are toate obiectele pentru căutare.
Interpretorul trebuie sa ridice o eroare setata de voi în cazul în care este apelat
obiectul prin len(). Setati 3 obiecte și testați functionalitatea.
"""


class Util:
    lista = []

    def __init__(self):
        Util.lista.append(self)


class Izatori:
    def __init__(self, user, passw):
        self.user = user
        self.passw = passw


class Utilizatori(Util, Izatori):
    def __init__(self, user, passw):
        Util.__init__(self)
        Izatori.__init__(self, user, passw)

    def __str__(self):
        return f"Utilizatori: {self.user}"

    def __parole(self):
        set_obiecte = set()
        for i in Util.lista:
            set_obiecte.add(i.passw)
        return set_obiecte

    def __useri(self):
        set_obiecte = set()
        for i in Util.lista:
            set_obiecte.add(i.user)
        return set_obiecte

    def obtine_parole(self):
        return self.__parole()

    def obtine_utilizatori(self):
        return self.__useri()


obiect1 = Utilizatori("Dan Popescu", "abracadabra")
obiect2 = Utilizatori("Radu Ionescu", "popescu")
obiect3 = Utilizatori("Elena Ionescu", "clase")
print(obiect1)
print(obiect2)
print(obiect3)
print(obiect1.obtine_parole())
print(obiect1.obtine_utilizatori())
