//This the Quicksort algorithm in JS.



//swap function
function swap(arr, left, right) {
  var temp = arr[left];
  arr[left] = arr[right];
  arr[right] = temp;
}

//partition function
function partition(arr, left, right) {
  var pivot = arr[Math.floor((left + right) / 2)];
  var i = left;
  var j = right;

  while (i <= j) {
    while (arr[i] < pivot) {
      i++;
    }
    while (arr[j] > pivot) {
      j--;
    }
    if (i <= j) {
      swap(arr, i, j);
      j--;
      i++;
    }
  }
  return i;
}

//sort function
function sort(arr, left, right) {
  var index;
  if (arr.length > 1) {
    index = partition(arr, left, right);
    if (left < index - 1) {
      sort(arr, left, index - 1);
    }
    if (index < right) {
      sort(arr, index, right);
    }
  }
  return arr;
}
//driver code
var unsorted = [53, -68, 14, -52, -37, 10, -1, -55, -37, -23, 12, 46, -50, 45, -9, -32, -40, -60, 50, -32, -22, -15, -29, 2, 41, -18, 13, 56, 14, 32, -21, -41, 40, -30, -19, 35, -10, 46, -24, 37, -54, 3, -20, 28, -29, 41, 60, 59, -10, 28]
console.log(sort(unsorted, 0, unsorted.length - 1));
