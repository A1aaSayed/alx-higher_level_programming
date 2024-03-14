#!/usr/bin/node

const { argv } = require('process');
const str = 'C is fun';
const n = parseInt(argv[2]);

if (isNaN(n) || argv.length === 2) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < n; i++) {
    console.log(str);
  }
}
