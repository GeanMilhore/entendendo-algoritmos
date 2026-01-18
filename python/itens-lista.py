def contar(lista = []):
    length = 0
    if len(lista) == 0:
        return 0
    else:
        length += 1
        del lista[0]
        return length + contar(lista)
    
print(contar([]))

print(contar([1]))
    
print(contar([1,2,3]))

print(contar([1,2,3,1,1,1,1,1,1,1]))