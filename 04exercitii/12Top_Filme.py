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
persoana = None
numar_filme = 0
for i in lista_filme:
    if numar_filme < len(i['filme']):
        numar_filme = len(i['filme'])
        persoana = i['nume']
print(f'{persoana}: {numar_filme}')
