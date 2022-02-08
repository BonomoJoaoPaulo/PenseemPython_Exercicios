import math

def eval_func(expressao):
    return eval(expressao)


while True:
    entrada = input()
    if entrada != 'done':
        saida = eval_func(entrada)
        print(saida)
    else:
        print(saida)
        break
