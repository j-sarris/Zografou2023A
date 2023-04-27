def bubbleSort(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):

        for j in range(1, n):
            # Swap if the element found is greater
            # than the next element
            if arr[j] < arr[j - 1]:
                tmp = arr[j]
                arr[j]= arr[j-1]
                arr[j-1]=tmp
         
arr = [64, 34, 25, 12, 22, 11, 90]
 
bubbleSort(arr)

print("Sorted array is:", arr)
