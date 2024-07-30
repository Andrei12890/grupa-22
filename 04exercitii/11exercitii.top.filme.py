lista_filme = [
    {
        'nume': 'George',
        'filme': ['b', 'c']
    },
    {
        'nume': 'Cristian',
        'filme': ['b', 'c', 'd', 'e', 'a']
    },
    {
        'nume': 'Stefan',
        'filme': ['c', 'a', 'a']
    }
]
filme_vizionate = {

}

cel_mai_vizionat_film = []
numar_vizionari = 0

for utilizator in lista_filme:
    for film in utilizator['filme']:
        if film in filme_vizionate:
            filme_vizionate[film] = filme_vizionate[film] + 1
            # filme_vizionate[film] += 1
        else:
            filme_vizionate[film] = 1
        if numar_vizionari <= filme_vizionate[film]:
            numar_vizionari = filme_vizionate[film]
            if film not in cel_mai_vizionat_film:
                cel_mai_vizionat_film.append(film)
            for i in cel_mai_vizionat_film:
                if filme_vizionate[i] < numar_vizionari:
                    cel_mai_vizionat_film.remove(i)
                print(i)
print(filme_vizionate)
print(numar_vizionari)
print(cel_mai_vizionat_film)
