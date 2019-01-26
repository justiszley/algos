import random

def swapElements (arr, a, b):
    arr[a], arr[b] = arr[b], arr[a]

def selectionSort(arr):
    copyArr = list(arr);
    arrLength = len(copyArr)
    for i in range(arrLength):
        smallest = i
        for j in range(i + 1, arrLength):
            if copyArr[j] < copyArr[smallest]:
                smallest = j
        swapElements(copyArr, i, smallest)
    return copyArr

myList = random.sample(range(-5, 5), 10)
sortedArr = selectionSort(myList)
print(myList)
print(sortedArr)