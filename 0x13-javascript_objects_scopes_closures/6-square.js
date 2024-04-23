#!/usr/bin/node

class Square extends require('./5-square') {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    for (let i = 0; i < this.height; i++) {
        if (c === undefined) {
            console.log('X'.repeat(this.width));
        } else {
            console.log(c.repeat(this.width));
        }
    }
  }
}

module.exports = Square;
