# Time Complexity:
    # Worst: n^2
    # Best: n
    # Average: n^2
# Space Complexity: 1
# The insertion sort is used when:
    # the array is has a small number of elements
    # there are only a few elements left to be sorted
def insertionSort(array):
    for step in range(1, len(array)):
        key = array[step]
        j = step - 1

        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        
        array[j+1] = key

    return array

# Time Complexity:
    # Worst: n^2
    # Best: n
    # Average: n^2
# Space Complexity: 1 (2 variables used)
# Bubble sort is used if
    # complexity does not matter
    # short and simple code is preferred
def bubbleSort(array):
    swapped = False
    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                swapped = True
            if not swapped:
                break
    return array

# Time Complexity:
    # Worst: n^2
    # Best: n^2
    # Average: n^2
# Space Complexity: 1
# The selection sort is used when
    # a small list is to be sorted
    # cost of swapping does not matter
    # checking of all the elements is compulsory
    # cost of writing to a memory matters like in flash memory (number of writes/swaps is O(n) as compared to O(n2) of bubble sort)
def selectionSort(array):
    for step in range(len(array)):
        min_idx = step

        for i in range(step + 1, len(array)):
            if array[i] < array[min_idx]:
                min_idx = i

        array[step], array[min_idx] = array[min_idx], array[step]
    return array

# Usage
print(insertionSort([9, 5, 1, 4, 3]))
print(bubbleSort([9, 5, 1, 4, 3]))
print(selectionSort([9, 5, 1, 4, 3]))