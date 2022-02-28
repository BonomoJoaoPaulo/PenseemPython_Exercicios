def any_lowercase2(s):
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'


word = 'BANANA'

print(any_lowercase2(word))

# ERRO: A funcao sempre retorna 'True'.
# Independente do que se escreve, o programa sempre retornarah 'True', jah que ele estah
# analisando se o caracter 'c' eh minusculo, não a variavel c dentro da string s.
