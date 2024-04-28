#!/usr/bin/node

exports.esrever = function (list) {
  reversed = [];
  for (let i = list.lenght; i > 0; i--) {
    reversed.push (list[i]);
  }
  return reversed;
};
