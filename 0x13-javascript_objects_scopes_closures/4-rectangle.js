#!/usr/bin/node

/**
 * Rectangle class representation
 *
 * @class Rectangle
 */
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
    // otherwise, empty object
  }

  print () {
    // prints the rectangle using the character X
    for (let h = 0; h < this.height; h++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    // exchanges the width and the height of the rectangle
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  double () {
    // multiples the width and the height of the rectangle by 2
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
