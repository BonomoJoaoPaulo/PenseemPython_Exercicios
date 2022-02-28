def any_lowercase1(s):
    for c in s:
        if c.islower():
            return True
        else:
            return False


word = 'Banana'

print(any_lowercase1(word))

# ERRO: A funcao soh será executada para a primeira letra da palavra.
# Se escrevermos 'Banana', o programa retorna 'False', jah que o indice 0 tem a letra maiuscula.
# Isso estah incorreto pois o programa deveria retornar 'True', jah que as demais letras da palavra
# sao minusculas.
