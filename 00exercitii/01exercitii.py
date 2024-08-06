"""
Creează un program care găsește și afișează cuvântul cel mai lung într-o propoziție introdusă de utilizator.
"""
def long():
    propozitie = input("Introduceti propozitia")
    v = 0
    for cuvant in propozitie.split():
        if len(cuvant) > v:
            v = len(cuvant)
            lon = cuvant

    return lon

print(long())