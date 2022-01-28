
def recurse(n, s):
    """ n e s são dois inteiros para que
    caso n seja igual a 0, a função printará
    s. Do contrário, a função chamará ela mesma
    agora alterando n para n-1 e s para n+s até
    que n atinja o valor de 0.
    """
    if n == 0:
        print(s)
    else:
        recurse(n-1, n+s)

recurse(-1, 0)

# Se chamarmos a função com -1 e 0 como argumentos,
# haverá o seguinte erro de recursão:
# RecursionError: maximum recursion depth exceeded in comparison
# Isso ocorre pois a variável n nunca chegará ao valor 0,
# então a função será executada infinitamente.
# Ocorrerá uma Recursividade infinita.
