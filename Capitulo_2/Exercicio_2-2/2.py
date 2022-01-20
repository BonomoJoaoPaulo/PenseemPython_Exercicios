
preco_capa = 24.95
preco_desconto = preco_capa*0.4

def calcula_valor_exemplares_d(exemplares):
    valor_exemplares = preco_desconto * exemplares
    return valor_exemplares


def calcula_frete(exemplares):
    valor_frete = 0
    if exemplares >= 1:
        valor_frete = 3 + 0.75*(exemplares - 1)
    return valor_frete


total_livros = 60

ved = calcula_valor_exemplares_d(total_livros)
vf = calcula_frete(total_livros)
valor_total = ved + vf

print(f'Valor total: R$ {valor_total:.2f}')
