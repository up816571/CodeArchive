function add(a,b) {
  return a+b;
}
module.exports.add = add;

function compare(arr1, arr2) {
  if(arr1.length !== arr2.length) {
    return false;
  }
  for(let i = 0; i < arr1.length; i++ ) {
    if (arr1[i] !== arr2[i]) {
      return false;
    }
  }
  return true;
}

module.exports.compare = compare;

function largest(arrOfnumbers) {
  let largest = 0;
  for(let i = 0; i < arrOfnumbers.length; i++ ) {
    if (arrOfnumbers[i] > largest) {
      largest = arrOfnumbers[i];
    }
  }
  return largest;
}

module.exports.largest = largest;
