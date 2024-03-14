#!/usr/bin/node

function add(a, b) {
  return (a + b);
}

const { argv } = require('process');
const first = parseInt(argv[2]);
const second = parseInt(argv[3]);

const sum =  add(first, second);
console.log(sum);
