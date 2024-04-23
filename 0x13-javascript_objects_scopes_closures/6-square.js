#!/usr/bin/node

class Square extends require('./5-square') {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    for (let i = 0; i < this.size; i++) {
        if (c === undefined) {
            console.log('X'.repeat(this.size));
        } else {
            console.log(c.repeat(this.size))
        }
    }
  }
}

module.exports = Square;
