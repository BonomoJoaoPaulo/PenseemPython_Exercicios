def any_lowercase5(s):
    for c in s:
        if not c.islower():
            return False
    return True


word = 'bAnana'

print(any_lowercase5(word))

# ERRO: se alguma letra for maiuscula, jah basta para o programa retornar 'False'.
# Isso ocorre pois caso alguma letra nao seja lowercase a function entra na condicao e retorna 'False'.
# O codigo soh estah correto em casos em que todas as letras sejam lowercase.
