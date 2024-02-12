#!/usr/bin/node

// define add function
function add (a, b) {
  return a + b;
}

// get arguments
const firstArg = parseInt(process.argv[2]);
const secondArg = parseInt(process.argv[3]);

// call add function
const result = add(firstArg, secondArg);
console.log(result);
