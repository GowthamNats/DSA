# Time Complexity:
    # Worst: nlogn
    # Best: nlogn
    # Average: nlogn
# Space Complexity: n
# Merge Sort Applications
    # Inversion count problem
    # External sorting
    # E-commerce applications

def merge(array, l, m, r):
    n1, n2 = m - l + 1, r - m

    L, R = [0] * n1, [0] * n2

    for i in range(n1):
        L[i] = array[l + i]
    
    for j in range(n2):
        R[j] = array[m + 1 + j]
    
    i = 0
    j = 0
    k = l

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            array[k] = L[i]
            i += 1
        else:
            array[k] = R[j]
            j += 1
        k += 1
    
    while i < n1:
        array[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        array[k] = R[j]
        j += 1
        k += 1

def mergeSort(array, l, r):
    if l < r:
        m = l + (r - l)//2
        mergeSort(array, l, m)
        mergeSort(array, m + 1, r)
        merge(array, l, m, r)

array = [9, 5, 1, 4, 3]
mergeSort(array, 0, len(array) - 1)
print(array)