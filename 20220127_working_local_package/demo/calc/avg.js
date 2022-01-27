const sum = require('./sum');

let avg = (list) => {
  console.log('pog update');
  return sum(list) / list.length;
}

module.exports = avg;
