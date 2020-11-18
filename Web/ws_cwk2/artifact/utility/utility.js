function removeFromArray(arr, index) {
  return arr.filter((item, checkedItem) => {return checkedItem != index});
}

module.exports.removeFromArray = removeFromArray;
