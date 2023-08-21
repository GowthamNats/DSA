def linearSearch(array, data):
    for i in range(len(array)):
        if array[i] == data:
            return i
    return False

def binarySearch(array, data, l, r):
    if l > r:
        return False
    else:
        mid = (l + r)//2
        if data == array[mid]:
            return mid
        elif data > array[mid]:
            return binarySearch(array, data, mid + 1, r)
        else:
            return binarySearch(array, l, mid - 1)

array = [2, 4, 0, 1, 9]
print(linearSearch(array, 1))
print(binarySearch(array, 1, 0, len(array)-1))