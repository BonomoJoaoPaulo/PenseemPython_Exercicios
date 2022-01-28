
def is_triangule(a, b, c):
    lados = [a, b, c]
    for x in lados:
        if x > (sum(lados) - x):
            return "No"
    return "Yes"


gravetoA, gravetoB, gravetoC = [int(x) for x in input("Informe o tamanho dos gravetos: ").split()]

print(is_triangule(gravetoA, gravetoB, gravetoC))
