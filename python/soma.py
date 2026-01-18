def soma(lista = []):
    if len(lista) == 0:
        return 0
    else:
        number = lista[0]
        del lista[0]
        return number + soma(lista)
    
print(soma([]))
    
print(soma([5]))

print(soma([5,4,9,12]))