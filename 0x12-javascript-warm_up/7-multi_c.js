#!/usr/bin/node

const { argv } = require("process");

const x = parseInt(argv[2]);

if (isNaN(x) || argv[2] == 2) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
}
