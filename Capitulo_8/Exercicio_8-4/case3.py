def any_lowercase3(s):
    for c in s:
        flag = c.islower()
    return flag


word = 'bananA'

print(any_lowercase3(word))

# ERRO: A funcao sempre retorna se a ultima letra eh minuscula, pois ele estah alterando o valor de 'flag'
# para toda vez que excecuta um caracter da string (alterando pela ultima vez na ultima letra).
# Se escrevermos 'bananA', o programa retorna 'False', jah que o indice -1 tem a letra maiuscula.
# Isso estah incorreto pois o programa deveria retornar 'True', jah que as demais letras da palavra
# sao minusculas.
