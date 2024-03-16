#!/usr/bin/node
function computeFactorial (num) {
  if (num == 0 || isNaN(num)) {
    return 1;
  }
  return num * computeFactorial(num - 1);
}

console.log(computeFactorial(process.argv[2]));
