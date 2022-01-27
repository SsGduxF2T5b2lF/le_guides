let avg = (list) => {
  let sum = list.reduce((a,b) => a + b);
  return sum / list.length;
}

export default avg;
