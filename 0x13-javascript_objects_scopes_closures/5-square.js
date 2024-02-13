#!/usr/bin/node

const Rectangle = require('./4-rectangle');

/**
 * Square class representation - inherits from Rectangle class
 *
 * @class Square
 */
class Square extends Rectangle {
  constructor (size) {
    super(size, size); // call parent constructor
  }
}

module.exports = Square;
