#!/usr/bin/node

// const { argv } = require('process');
const args = process.argv.slice(2)

if (args.length === 0 || args.length === 1) {
  console.log(0);
} else {
  const numbers = args.map((item) => parseInt(item));
  numbers.sort((a, b) => b - a)
  console.log(numbers[1]);
}
