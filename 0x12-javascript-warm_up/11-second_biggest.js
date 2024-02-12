#!/usr/bin/node
const args = process.argv;

let biggest = args[0];
let second;

// check user inputs
if (args.length < 4) {
  console.log(0);
  process.exit();
}

// loop through args vector
args.forEach((num) => {
  if (num > biggest) {
    second = biggest;
    biggest = num;
  }
  else if (num > second && num < biggest) {
    second = num;
  }
});

// print second biggest number
console.log(second);
