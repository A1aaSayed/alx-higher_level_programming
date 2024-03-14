#!/usr/bin/node

const { argv } = require('process');
const str = 'C is fun';
const n = parseInt(argv[2]);

if (isNaN(n) || argv.length === 2) {
  console.log('Missing number of occurrences');
} else {
    while (n !== 0) {
      if (n < 0) {
        break;
      }
      console.log(str);
      n--;
    }
}
