def insertion_sort(array):
    for i in range(1, len(array)):
        current = array[i]
        j = i - 1
        while (j >= 0 and array[j] > current):
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = current
 
 
array =  [5, 2, 7, 1, 5, 9, 8]
insertion_sort(array)
print('Sorted list: ', end='')
print(array)
