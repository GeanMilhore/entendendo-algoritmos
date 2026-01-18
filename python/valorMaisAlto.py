def buscarValorMaisAlto(lista = []):
    if len(lista) == 1:
        return lista[0]
    else:
        valor_atual = lista[0]
        del lista[0]
        valor_mais_alto = buscarValorMaisAlto(lista)

        return valor_atual if valor_atual > valor_mais_alto else valor_mais_alto

print(buscarValorMaisAlto([0, 12,132,499,3]))