#!/usr/bin/node

// define factorial function
function factorial (n) {
  // factorial(n) = n * factorial(n - 1)

  if (n < 0) { // negative number
    return -1
  }
  if (n === 0 || isNaN(n)) {
    return 1;
  }
  return n * factorial(n - 1);
}

// get arguments form argv
const arg = Number(process.argv[2]);

// call factorial function and print result
const result = factorial(arg ? arg : 0);
console.log(result);
