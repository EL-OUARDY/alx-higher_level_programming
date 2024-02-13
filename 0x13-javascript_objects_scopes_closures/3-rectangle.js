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

    print () {
        for (let h = 0; h < this.height; h++) {
            console.log('X'.repeat(this.width));
        }
    }
}

module.exports = Rectangle;
