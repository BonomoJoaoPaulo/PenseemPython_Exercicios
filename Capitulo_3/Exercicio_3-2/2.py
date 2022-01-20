
def do_twice(f, v):
    f(v)
    f(v)

def print_spam():
    print('spam')

do_twice(print_spam, 'test')

# Obs: Nao sei se isso ocorreu por erro de traducao,
# mas o enunciado deste exercicio estava muito confuso.
# Da forma que esta aqui, ele retorna erro, ja que estou
# passando um argumento para print_spam, sendo que essa funcao
# nao requer argumentos.
