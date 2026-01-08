list = [0, 1, 1, 2, 3, 5, 8, 13, 21]
item = 21

# returns the item postion
def binary_search(list, item):
    baixo = 0;
    alto = len(list);

    while baixo <= alto: 
        meio = (baixo + alto) // 2;
        chute = list[meio]

        if(chute == item):
            return meio;
        if(chute > item):
            alto = meio - 1;
        if(chute < item):
            baixo = meio + 1;

print(binary_search(list, item));