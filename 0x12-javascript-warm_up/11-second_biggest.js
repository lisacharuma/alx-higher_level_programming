#!/usr/bin/node
const argv = process.argv;
function secondMax (myArray) {
  if (myArray.length <= 3) {
    return (0);
  }

  myArray = myArray.slice(2).map(n => parseInt(n));

  const max = Math.max(...myArray);

  const arr = myArray.filter(arr => arr < max);

  return (Math.max(...arr));
}
console.log(secondMax(argv));
