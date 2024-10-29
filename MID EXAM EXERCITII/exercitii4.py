"""
Se dă un şir cu cel mult 10 caractere. Să se determine
câte vocale conţine.
"""


def numar_vocale(sir):
    vocale = "aeiouăîAEI"
    count = sum(1 for char in sir if char in vocale)
    return count


sir = input("Introduceți un șir de cel mult 10 caractere!: ")
if len(sir) <= 10:
    print("Numărul de vocale este: ", numar_vocale(sir))
else:
    print("Șirul introdus are mai mult de 10 caractere! Încearcă din nou!")
