#!/usr/bin/node
const size = parseInt(process.argv[2]);

// check if argument is a valid number
if (!size) {
  console.log('Missing size');
} else {
  // draw the square
  let iterator = size;
  while (iterator > 0) {
    console.log('X'.repeat(size));
    iterator--;
  }
}
