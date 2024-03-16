#!/usr/bin/node
function computeFactorial(num) {
  if (num == 0 || isNaN(num))
    return 1;
  return num * computeFactorial(num - 1);
}

const input = process.argv[2];
const number = parseInt (input);
const factorial = computeFactorial (number);

console.log(factorial);
