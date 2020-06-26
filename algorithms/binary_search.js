let sorted_list = [0, 1, 2, 3, 4, 5, 6,7,8,9,10,11,12,13,14,15,16,17,18,19,20];
//left is the index leftmost element, right is the index rightmost element
//arr is the array and elem is the element to be searched.
function search(left, right, arr, elem) {
  if (left > right) return false;

  let mid = Math.floor((left + right) / 2);
  if (arr[mid] == elem) {
    return mid;
  } else if (arr[mid] > elem) {
    return search(left, mid - 1, arr, elem);
  } else if (arr[mid] < elem) {
    return search(mid + 1, right, arr, elem);
  }
}

const binary_search = (arr,elem) =>{
    return search(0,arr.length-1,arr,elem);
}

console.log(binary_search(sorted_list,4.5));
