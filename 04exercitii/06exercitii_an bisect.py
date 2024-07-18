"""
3. Creati un program in care utilizatorul sa introduca un an. Calculati daca anul este
bisect sau nu si afisati un raspuns in acest sens. OBS. Un an bisect se imparte exact
la 4 (fara rest)
"""

an = input("introduceti un an: ")
if int('an') % 4 == 0:
    print("Anul este bisect")
else:
    print("Anul nu este bisect")
