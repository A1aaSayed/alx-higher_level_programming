#!/usr/bin/node

const { argv } = require('process');
const str = argv[2];
const num = Number(str);

if (isNaN(num)) {
  console.log('Not a number');
} else {
  console.profile('My number: ' + Math.floor(num));
}
