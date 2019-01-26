const arr = [];

// fill the array
for (let i = 0; i <= 10; i++) {
    const random = Math.round(Math.random(10) * 10 - 5);
    arr.push(random);
}

const sortedArr = selectionSort(arr);
console.log(arr);
console.log(sortedArr);

function selectionSort(arr) {
    const tempArr = [...arr];
    // because the last element is already on its place.
    const n = tempArr.length - 1;
    let smallest;

    for (let i = 0; i < n; i++) {
        smallest = i;

        for (let j = i + 1; j <= n; j++) {
            if (tempArr[j] < tempArr[smallest]) {
                smallest = j;
            }
        }

        swapElements(tempArr, i, smallest);
    }

    return tempArr;
}

function swapElements(arr, a, b) {
    const aVal = arr[a];
    arr[a] = arr[b];
    arr[b] = aVal;
}