# сортировка масива пузырьком 9, 6, 7, 2, 5, 1, 3, 4, 8, 0

def bubbleSorting(list):
    sort = 0
    for j in range(len(list) - 1):
        count = 0
        for i in range(len(list) - 1):
            sort += 1
            if list[i] > list[i + 1]:
                temp = list[i + 1]
                list[i + 1] = list[i]
                list[i] = temp
                count += 1
        if count == 0:
            break

    return list, sort


# print(bubbleSorting([9, 6, 7, 2, 5, 1, 3, 4, 8, 0]))


def quickSort(list, start, end):
    pivot = list[int((end - start) / 2 + start)]
    leftPosition = start
    rightPosition = end
    while leftPosition <= rightPosition:
        while list[leftPosition] < pivot:
            leftPosition += 1

        while list[rightPosition] > pivot:
            rightPosition -= 1

        if leftPosition <= rightPosition:
            if leftPosition < rightPosition:
                temp = list[leftPosition]
                list[leftPosition] = list[rightPosition]
                list[rightPosition] = temp
            leftPosition += 1
            rightPosition -= 1

    if start < rightPosition:
        quickSort(list, start, rightPosition)

    if end > leftPosition:
        quickSort(list, leftPosition, end)

    return list


array = [9, 4, 6, 15, 2, 200, 7, 0, 2, 125, 5, 1, 3, 4, 8, 1, 25, 0, 11]


print(quickSort(array, 0, len(array)-1))


def binarySearch(list, value, minNumber, maxNumber):
    # midpoint = 0
    if maxNumber < minNumber:
        return -1
    else:
        midpoint = int((maxNumber + minNumber) / 2)

    if list[midpoint] < value:
        return binarySearch(list, value, midpoint + 1, maxNumber)
    else:
        if list[midpoint] > value:
            return binarySearch(list, value, minNumber, midpoint - 1)
        else:
            return midpoint

    return -1


# newArray = quickSort(array, 0, len(array) - 1)
# print(newArray)
# print(binarySearch(newArray, 9, 0, len(newArray)))


def pyramidSorting(list):
    for i in range(int(len(list) / 2) - 1, -1, -1):
        heap(list, len(list), i)

    for i in range(len(list) - 1, -1, -1):
        temp = list[0]
        list[0] = list[i]
        list[i] = temp
        heap(list, i, 0)
    return list


def heap(arr, heapSize, rootIndex):
    largest = rootIndex
    leftChild = 2 * rootIndex + 1
    rightChild = 2 * rootIndex + 2

    if leftChild < heapSize and arr[leftChild] > arr[largest]:
        largest = leftChild
    if rightChild < heapSize and arr[rightChild] > arr[largest]:
        largest = rightChild

    if largest != rootIndex:
        temp = arr[rootIndex]
        arr[rootIndex] = arr[largest]
        arr[largest] = temp

        heap(arr, heapSize, largest)


print(pyramidSorting(array))
