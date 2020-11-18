const _ =require('underscore');

function range(numberArray) {
  return _.max(numberArray) - _.min(numberArray);
}

module.exports.range = range;
