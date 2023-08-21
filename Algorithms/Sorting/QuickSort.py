# Time Complexity:
    # Worst: nlogn
    # Best: n^2
    # Average: nlogn
# Space Complexity: logn
# Quicksort algorithm is used when
    # the programming language is good for recursion
    # time complexity matters
    # space complexity matters
def partition(array, l, r):
    pivot = array[r]
    store_idx = l - 1
    for i in range(l, r):
        if array[i] <= pivot:
            store_idx += 1
            array[i], array[store_idx] = array[store_idx], array[i]
    array[r], array[store_idx + 1] = array[store_idx + 1], array[r]
    return store_idx + 1

def quickSort(array, l, r):
    if l < r:
        pivot = partition(array, l, r)
        quickSort(array, l, pivot - 1)
        quickSort(array, pivot + 1, r)

array = [9, 5, 1, 4, 3]
quickSort(array, 0, len(array) - 1)
print(array)