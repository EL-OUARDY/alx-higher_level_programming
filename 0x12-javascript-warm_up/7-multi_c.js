#!/usr/bin/node
let nbTimes = parseInt(process.argv[2]);

// check if argument is a valid number
if (!nbTimes) {
  console.log('Missing number of occurrences');
} else {
  // loop through array items
  while (nbTimes > 0) {
    console.log('C is fun');
    nbTimes--;
  }
}
