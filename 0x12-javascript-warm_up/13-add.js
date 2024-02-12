#!/usr/bin/node

// define add function
function add(a, b) {
  return a + b;
}

// make add function available to the outside
module.exports.add = add;
