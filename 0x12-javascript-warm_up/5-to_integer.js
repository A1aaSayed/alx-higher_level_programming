#!/usr/bin/node

const { argv } = require('process');
const str = argv[2];
const num = parseInt(str);

if (isNaN(num)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + Math.floor(num));
}
