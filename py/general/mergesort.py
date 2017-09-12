def mergesort(array):
    helper = [0] * len(array)
    _mergesort(array, helper, 0, len(array)- 1)

def _mergesort(array, helper, low, high):
    if low < high:
        middle = (low + high) // 2
        _mergesort(array, helper, low, middle)
        _mergesort(array, helper, middle + 1, high)
        merge(array, helper, low, middle, high)

def merge(array, helper, low, middle, high):
    for i in range(low, high + 1):
        helper[i] = array[i]

    helperLeft = low
    helperRight = middle + 1
    current = low

    while helperLeft <= middle and helperRight <= high:
        if helper[helperLeft] <= helper[helperRight]:
            array[current] = helper[helperLeft]
            helperLeft += 1
        else:
            array[current] = helper[helperRight]
            helperRight += 1
        current += 1

    remaining = middle - helperLeft
    for i in range(remaining + 1):
        array[current + i] = helper[helperLeft + i]

a = [1,10,9,7,4,5,2,1,8,3,2,1]
mergesort(a)
print(a)
