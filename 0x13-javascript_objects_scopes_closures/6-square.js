#!/usr/bin/node

const XSquare = require('./5-square');

/**
 * Square class representation - inherits from XSquare (old Square class)
 *
 * @class Square
 */
class Square extends XSquare {
  constructor (size) {
    super(size); // call parent constructor
  }

  charPrint (c) {
    // set a default character if c is undefined
    c = c ? c : 'X';
    // prints the rectangle using the given character
    for (let h = 0; h < this.height; h++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;
