#!/usr/bin/node

const { argv } = require('process');
const first = parseInt(argv[2]);
const second = parseInt(argv[3]);
const sum =  add(first, second);

console.log(sum);

function add(a, b) {
  return a + b;
}
