import random

def swapElements (arr, a, b):
    aVal = arr[a]
    arr[a] = arr[b]
    arr[b] = aVal

myList = random.sample(range(-5, 5), 10)
print(myList)

for i in range(10):
    smallest = i
    j = i + 1
    for m in range(10 - (1+i)):
        if myList[j] < myList[smallest]:
            smallest = j;
        j += 1;
    swapElements(myList, i, smallest)

print(myList)