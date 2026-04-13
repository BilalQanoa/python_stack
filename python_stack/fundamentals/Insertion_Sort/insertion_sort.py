
def insertion_sort(lista):
    for i in range(1, len(lista)):
        key = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > key:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = key
    return lista


test_list = [12, 11, 13, 5, 6]
print(insertion_sort(test_list))
