
def selection_sort (lista):
    n = len(lista)
    for i in range(n):
        min_index = i
        for j in range (i+1, n):
            if lista[j] < lista[min_index]:
                min_index = j
        lista[i], lista[min_index] = lista[min_index], lista[i]
    return lista

numbers = [64, 25, 12, 22, 11]
print("Original array:", numbers)
sorted_numbers = selection_sort(numbers)
print("Sorted array:", sorted_numbers)