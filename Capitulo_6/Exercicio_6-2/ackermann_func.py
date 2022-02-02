# Veja: http://en.wikipedia.org/wiki/Ackermann_function

def ackermann_func(m, n):
    if m == 0:
        return n+1

    if n == 0:
        return ackermann_func(m-1, 1)

    if m > 0 and n > 0:
        return ackermann_func(m-1, ackermann_func(m, n-1))


print(ackermann_func(3, 4))

# Caso colequemos valores maiores para m e n (exemplo: m = 4, n = 5)
# o máximo de recursões será atingido e teremos
# o seguinte erro exibido no terminal:
# RecursionError: maximum recursion depth exceeded in comparison
