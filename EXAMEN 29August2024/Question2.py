"""
Scrie o functie care sa numere cate elemente pozitive sunt intr-un tuplu dat.
Exemplu de Input si Output:
Input: tuple_example = (-1,3,-2,4,0)
Output: result = 2 (deoarece sunt 2 numere pozitive: 3 si 4)
(1 punct)
"""

tuple_example = (-1, 3, -2, 4, 0)


def elemente_pozitive(tuple_example):
    count = 0
    for numar in tuple_example:
        if numar > 0:
            count += 1
    return count


result = elemente_pozitive(tuple_example)
print(result)
