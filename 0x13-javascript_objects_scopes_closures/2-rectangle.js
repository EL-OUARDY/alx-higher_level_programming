#!/usr/bin/node

/**
 * Rectangle class representation
 *
 * @class Rectangle
 */
class Rectangle {
    constructor(w, h) {
        if (w > 0 && h > 0) {
            this.width = w;
            this.height = h;
        }
        // otherwise, empty object
    }
}

module.exports = Rectangle;
