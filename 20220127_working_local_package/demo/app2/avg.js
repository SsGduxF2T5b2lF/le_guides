const sum = require('./sum');

let avg = (list) => {
  return sum(list) / list.length;
}

module.exports = avg;
